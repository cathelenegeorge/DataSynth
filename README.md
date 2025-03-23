# 📊 DataSynth & DataWiz - AI-Powered Dataset Generation & Analysis Suite

## 🚀 Introduction

In the world of **Artificial Intelligence (AI) and Machine Learning (ML)**, high-quality datasets and effective data analysis are crucial for building robust models. However, **finding, curating, structuring, and analyzing datasets** is often a challenge.

Our **AI-Powered Dataset Suite**, featuring **DataSynth** and **DataWiz**, provides a seamless end-to-end solution for **dataset generation, transformation, analysis, and visualization**.

- **DataSynth** generates structured, context-aware datasets using **OpenAI's GPT-4**, eliminating the need for manual data collection and preprocessing.
- **DataWiz** transforms raw data into actionable insights using **AI-powered data processing, statistical analysis, and intelligent visualization**.

Together, these tools **simplify the data pipeline** for Data Scientists, Analysts, and AI/ML Engineers. 🚀

---

# 📌 DataSynth - AI-Powered Dataset Generator

## ❌ The Problem: Dataset Challenges

🔴 **Finding relevant datasets**: Public datasets may not always match specific requirements.  
🔴 **Data cleaning & formatting**: Datasets often require preprocessing, leading to additional effort.  
🔴 **Missing values & inconsistencies**: Many datasets have missing or inconsistent data.  
🔴 **Time-consuming data collection**: Manually curating datasets is slow and tedious.  

---

## ✅ Our Solution: AI-Powered Dataset Generator

✨ Our tool allows users to simply **describe the dataset context**, specify the number of rows and columns, and instantly generate a structured dataset—complete with a **title, summary, and downloadable CSV format**.

### **🔥 Key Features:**
✅ **AI-Generated Dataset Titles**: Meaningful dataset titles based on the context.  
✅ **Smart Data Structuring**: Consistent formatting with **S.No (Serial Number)** and **Target** columns.  
✅ **Customizable Columns & Rows**: Users can specify the dataset size.  
✅ **AI-Powered Summary**: Provides insightful dataset explanations.  
✅ **Instant CSV Download**: Export datasets in **CSV format** for immediate use.  
✅ **Auto-Fixing Missing Values**: Ensures clean datasets with automatic fixes.  
✅ **User-Friendly & Interactive UI**: Built using **Streamlit** for a seamless experience.  

---

## 🎯 How DataSynth Works

1️⃣ **User Inputs:**
   - Number of Rows  
   - Number of Feature Columns  
   - Dataset Context (e.g., "Customer purchase data with date, product, and price")  

2️⃣ **AI Processing:**
   - Generates a **relevant dataset title**.  
   - Creates a **5-7 line summary**.  
   - Constructs a **fully formatted dataset** in CSV format.  

3️⃣ **User Output:**
   - **Dataset Title** displayed in bold.  
   - **Dataset Summary** shown as an info box.  
   - **Dataset Preview** displayed in a table.  
   - **CSV Download Button** for easy export.  

---

# 📌 DataWiz - AI-Powered Data Analysis & Visualization Tool

## ❌ The Problem: Data Analysis Challenges

🔴 **Raw datasets require preprocessing** before meaningful insights can be drawn.  
🔴 **Categorical data must be converted** into numerical form for ML applications.  
🔴 **Choosing the right visualization** method can be confusing and time-consuming.  
🔴 **Summary statistics must be computed manually**, which is inefficient.  
🔴 **Non-interactive dashboards** make exploration difficult.  

---

## ✅ Our Solution: AI-Powered Data Analysis & Visualization

**DataWiz automates and simplifies** these challenges using AI-driven techniques.

### **🔥 Key Features:**
✅ **Automated Data Transformation**: Converts categorical columns into numerical values.  
✅ **AI-Generated Summary Statistics**: Computes **5 key statistical insights**.  
✅ **NLP-Based Column Selection**: AI suggests the most relevant columns.  
✅ **AI-Powered Visualization**: Recommends **the best visualization technique**.  
✅ **📊 Interactive Charts & Graphs**: Generates **5 dynamic visualizations**.  
✅ **Seamless Integration with DataSynth**: Directly analyze generated datasets.  
✅ **📜 PDF & CSV Export**: Export transformed data, visualizations, and reports.  
✅ **User-Friendly & Interactive UI**: Built with **Streamlit** for real-time updates.  

---

## 🎯 How DataWiz Works

1️⃣ **User Inputs:**
   - Upload a dataset (CSV format) or load from **DataSynth**.  
   - Choose a **column transformation option** (categorical → numeric conversion).  
   - Enter a query to let **AI select relevant columns**.  
   - Select a **preferred visualization method** or let AI decide.  

2️⃣ **AI Processing:**
   - Cleans & transforms **categorical data into numerical format**.  
   - Computes **5 statistical insights**: mean, median, standard deviation, min, and max.  
   - Identifies the **best visualization method** based on column types.  

3️⃣ **User Output:**
   - **Dataset Preview** after transformation.  
   - **Summary statistics** displayed intuitively.  
   - **AI-recommended & user-selected charts**.  
   - **CSV & PDF Download Options**.  

---

# 🏗️ Tech Stack

- **💻 Frontend**: Streamlit (for an interactive UI)  
- **🤖 AI Engine**: OpenAI GPT-4 (for NLP-based dataset generation & column selection)  
- **📊 Data Processing**: Pandas & NumPy (for transformations & statistics)  
- **📂 File Handling**: CSV & PDF (for exports)  
- **📈 Visualization**: Matplotlib & Seaborn (for graphs & charts)  

---

# 🔧 Installation & Setup

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/your-repo/datasynth-datawiz.git
cd datasynth-datawiz
```

### 2️⃣ Install Dependencies
Ensure **Python 3.8+** is installed, then run:
```sh
pip install -r requirements.txt
```

### 3️⃣ Run the Application
```sh
streamlit run app.py
```

Access the web app at **[http://localhost:8501](http://localhost:8501)** 🎉

---

# 📢 Contributing
We welcome contributions! If you'd like to improve this project, please **fork the repository** and submit a pull request.

---

# 📝 License
This project is licensed under the **MIT License**.



