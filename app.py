import streamlit as st

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="BioInsight AI",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# Home Page
# --------------------------------------------------
st.title("🧬 BioInsight AI")
st.subheader("AI-Powered Gene Expression Analysis Dashboard")

st.markdown("---")

st.markdown("""
## 👋 Welcome!

**BioInsight AI** is a bioinformatics dashboard developed using **Python** and **Streamlit** for exploring and analyzing **gene expression datasets**.

This application provides an easy-to-use interface for data exploration, visualization, machine learning, and report generation.

---

## 🚀 Features

### 📂 Data Explorer
- View cleaned gene expression dataset
- Dataset preview
- Dataset statistics
- Gene Search

### 📊 Interactive Visualizations
- Correlation Heatmap
- Box Plot
- Violin Plot
- Interactive Plotly Charts

### 🤖 Machine Learning
- Principal Component Analysis (PCA)
- K-Means Clustering
- Random Forest Classification
- Feature Importance

### 🧬 Differential Gene Expression
- Top 20 Highly Expressed Genes
- Interactive Bar Chart
- Download Differential Expression Results

### 📄 Reports
- Download Cleaned Dataset (CSV)
- Generate Professional PDF Report

---

## 🛠️ Technologies Used

- 🐍 Python
- 🎈 Streamlit
- 🐼 Pandas
- 🔢 NumPy
- 📊 Plotly
- 📈 Matplotlib
- 🌊 Seaborn
- 🤖 Scikit-learn
- 📄 FPDF2

---

## 📖 How to Use

1. Open **Data Explorer** to inspect the dataset.
2. Use **Visualizations** to explore expression patterns.
3. Visit **Machine Learning** for PCA and clustering analysis.
4. Open **Differential Expression** to identify highly expressed genes.
5. Download reports from the **Report** page.

---

## 📌 Dataset

**Dataset:** GEO - GSE45827

Gene expression data used for bioinformatics analysis.

---

### 👈 Use the sidebar to navigate through the application.
""")

st.success("✅ BioInsight AI is running successfully!")

st.info("💡 Select any page from the left sidebar to begin your analysis.")

st.markdown("---")

st.caption("© 2026 BioInsight AI | Developed by Soumya Priyadarshini")