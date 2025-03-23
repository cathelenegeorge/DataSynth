import streamlit as st
import openai
import pandas as pd
import os
import csv
import io
import re

# Set OpenAI API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    st.error("❌ API key is missing! Please set OPENAI_API_KEY in your environment variables.")
    st.stop()

# Initialize OpenAI client
client = openai.OpenAI(api_key=OPENAI_API_KEY)

# Streamlit UI
st.title("📊 AI-Powered Dataset Generator")
st.markdown("""
👋 **Welcome to the AI-Powered Dataset Generator!**  
This tool allows you to **generate structured datasets** instantly using AI.  
Simply describe the dataset you need, specify the number of rows & columns, and let AI do the rest!  

🔹 **Features:**  
✅ Automatically generates datasets based on your context  
✅ Includes a **Target column** for easy classification tasks  
✅ Supports **CSV download **  

💡 *Try it now and create a dataset in seconds!* 🚀
""")

# User inputs
num_rows = st.number_input("🔢 Number of Rows", min_value=1, value=5)
num_cols = st.number_input("🔢 Number of Feature Columns (excluding S.No & Target)", min_value=1, value=3)
context = st.text_area("💡 Describe the dataset context (e.g., 'Sales data with Date, Product, and Price')")

if st.button("🚀 Generate Dataset"):
    with st.spinner("⏳ Generating dataset..."):
        # AI Prompt
        prompt = f"""
        Generate a structured dataset based on the following context:
        {context}

        **Dataset Requirements:**
        - **Title:** Provide only the dataset title.
        - **Summary:** Provide a short summary (5-7 lines).
        - **Data Table Format:**
          - {num_rows} rows.
          - {num_cols} feature columns.
          - First column: 'S.No' (Serial Number).
          - Last column: 'Target' (Categorical: 'Presence' or 'Absence').
        - **Output Format:**
          - Start with "**Title:** [dataset title]".
          - Then "### Dataset Summary" followed by a 5-7 line summary.
          - Then output structured data in **pure CSV format** (comma-separated, no extra text).
        """

        try:
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[{"role": "user", "content": prompt}]
            )

            # Extract response text
            raw_text = response.choices[0].message.content.strip()

            # **Extract Title**
            title_match = re.search(r"\*\*Title:\*\* (.*?)\n", raw_text)
            dataset_title = title_match.group(1).strip() if title_match else "Untitled Dataset"

            # **Extract Summary**
            summary_match = re.search(r"### Dataset Summary\n(.*?)\n\n", raw_text, re.DOTALL)
            summary_text = summary_match.group(1).strip() if summary_match else "Summary not available."

            # **Extract CSV Data**
            dataset_start = raw_text.find("S.No,")
            if dataset_start == -1:
                st.error("❌ AI-generated dataset format is incorrect. Please try again.")
                st.stop()

            csv_text = raw_text[dataset_start:]  # Extract only CSV part

            # **Parse CSV**
            csv_buffer = io.StringIO(csv_text)
            reader = csv.reader(csv_buffer)
            structured_data = list(reader)

            if len(structured_data) < 2:
                st.error("❌ AI-generated dataset format is incorrect. Please try again.")
                st.stop()

            # **Ensure Data Consistency & Handle Null Values**
            headers = structured_data[0]
            num_columns = len(headers)

            cleaned_data = [
                row[:num_columns] if len(row) > num_columns else row + ["N/A"] * (num_columns - len(row))
                for row in structured_data[1:]
            ]

            df = pd.DataFrame(cleaned_data, columns=headers)

            # **Handle missing values properly**
            df.fillna("N/A", inplace=True)
            df.replace("", "N/A", inplace=True)
            df.dropna(axis=1, how="all", inplace=True)  # Remove empty columns
            df.dropna(axis=0, how="all", inplace=True)  # Remove empty rows

            # **Display Dataset Title**
            st.markdown(f"### 📌 **{dataset_title}**")

            # **Display AI-generated Summary**
            st.markdown("### 📜 Dataset Summary")
            st.info(summary_text)

            # **Display Dataset Preview**
            st.subheader("📋 Dataset Preview")
            st.dataframe(df)

            # **Download CSV**
            csv_output = df.to_csv(index=False, lineterminator="\n").encode("utf-8")
            st.download_button("📥 Download CSV", csv_output, f"{dataset_title.replace(' ', '_')}.csv", "text/csv")

        except Exception as e:
            st.error(f"❌ An error occurred: {str(e)}")
