import streamlit as st

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="BioInsight AI",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("🧬 BioInsight AI")
st.sidebar.success("Gene Expression Analysis Dashboard")

# -----------------------------
# Header
# -----------------------------
st.title("🧬 BioInsight AI")
st.subheader("AI-Powered Gene Expression Analysis Dashboard")

st.markdown("""
Welcome to **BioInsight AI**, a web-based bioinformatics platform developed for exploring and analyzing gene expression datasets using modern data science and machine learning techniques.
""")

st.divider()

# -----------------------------
# Dashboard Metrics
# -----------------------------
st.header("📊 Dashboard Overview")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("🧬 Genes", "54,675")

with col2:
    st.metric("🧪 Samples", "130")

with col3:
    st.metric("📄 Reports", "PDF + CSV")

with col4:
    st.metric("🤖 ML Models", "3")

st.divider()

# -----------------------------
# Features
# -----------------------------
st.header("🚀 Features")

col1, col2 = st.columns(2)

with col1:

    st.info("""
### 📂 Data Explorer

- View Gene Expression Dataset
- Dataset Preview
- Summary Statistics
- Gene Search
""")

    st.success("""
### 📊 Interactive Visualizations

- Correlation Heatmap
- Box Plot
- Violin Plot
- Plotly Interactive Charts
""")

    st.warning("""
### 🤖 Machine Learning

- Principal Component Analysis (PCA)
- K-Means Clustering
- Random Forest Classification
- Feature Importance
""")

with col2:

    st.info("""
### 🧬 Differential Expression

- Top 20 Highly Expressed Genes
- Interactive Plotly Bar Chart
- CSV Download
""")

    st.success("""
### 📄 Report Generation

- Dataset Summary
- CSV Export
- Professional PDF Report
""")

    st.warning("""
### ℹ️ About

- Project Information
- Dataset Details
- Technologies Used
- Developer Profile
""")

st.divider()

# -----------------------------
# Workflow
# -----------------------------
st.header("🔬 Analysis Workflow")

st.code("""
      GEO Dataset
           │
           ▼
   Data Cleaning
           │
           ▼
   Data Exploration
           │
           ▼
 Interactive Visualization
           │
           ▼
 Machine Learning Analysis
           │
           ▼
 Differential Expression
           │
           ▼
 PDF & CSV Reports
""")

st.divider()

# -----------------------------
# Technologies
# -----------------------------
st.header("🛠️ Technologies Used")

tech1, tech2, tech3 = st.columns(3)

with tech1:
    st.markdown("""
✅ Python

✅ Streamlit

✅ Pandas

✅ NumPy
""")

with tech2:
    st.markdown("""
✅ Plotly

✅ Matplotlib

✅ Seaborn

✅ Scikit-learn
""")

with tech3:
    st.markdown("""
✅ FPDF2

✅ Git

✅ GitHub

✅ Streamlit Cloud
""")

st.divider()

# -----------------------------
# Dataset
# -----------------------------
st.header("🧬 Dataset")

st.success("""
**Dataset Source:** Gene Expression Omnibus (GEO)

**Dataset ID:** GSE45827

This dataset contains gene expression profiles used for bioinformatics analysis, visualization, and machine learning.
""")

st.divider()

# -----------------------------
# Developer
# -----------------------------
st.header("👩‍💻 Developer")

st.info("""
**Soumya Priyadarshini**

BioInsight AI was developed as a bioinformatics dashboard using Python and Streamlit.

It demonstrates data preprocessing, visualization, machine learning, differential gene expression analysis, and automated report generation.
""")

st.divider()

# -----------------------------
# Future Scope
# -----------------------------
st.header("🚀 Future Enhancements")

future1, future2 = st.columns(2)

with future1:
    st.markdown("""
- 🔬 Pathway Analysis
- 🧬 Gene Enrichment Analysis
- 🧪 Disease Classification
- ☁️ Cloud Database Integration
""")

with future2:
    st.markdown("""
- 🤖 Deep Learning Models
- 📈 Advanced Analytics
- 🔐 User Authentication
- 🌐 Multi-Dataset Support
""")

st.divider()

# -----------------------------
# Footer
# -----------------------------
st.markdown(
    """
    <div style='text-align:center; padding:20px;'>
        <h3>🧬 BioInsight AI</h3>
        <p>AI-Powered Gene Expression Analysis Dashboard</p>
        <p><b>Developed by Soumya Priyadarshini</b></p>
        <p>Built with ❤️ using Python, Streamlit, Plotly & Scikit-learn</p>
        <p>© 2026 BioInsight AI</p>
    </div>
    """,
    unsafe_allow_html=True
)