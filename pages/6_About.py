import streamlit as st

st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide"
)

st.title("ℹ️ About BioInsight AI")

st.markdown("""
# 🧬 BioInsight AI

BioInsight AI is a bioinformatics web application developed using **Python** and **Streamlit** for analyzing gene expression datasets.

The application helps researchers and students explore gene expression data through interactive visualizations, machine learning techniques, and downloadable reports.

---
""")

st.header("🎯 Project Objectives")

st.markdown("""
- Analyze gene expression datasets
- Visualize biological data interactively
- Apply machine learning techniques
- Identify highly expressed genes
- Generate downloadable analysis reports
""")

st.header("🧪 Dataset")

st.markdown("""
**Dataset Source:** Gene Expression Omnibus (GEO)

**Dataset Used:** GSE45827

This dataset contains gene expression profiles that can be explored using various statistical and machine learning techniques.
""")

st.header("⚙️ Technologies Used")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
- 🐍 Python
- 🎈 Streamlit
- 🐼 Pandas
- 🔢 NumPy
- 📈 Matplotlib
""")

with col2:
    st.markdown("""
- 📊 Plotly
- 🌊 Seaborn
- 🤖 Scikit-learn
- 📄 FPDF2
- 🔧 Git & GitHub
""")

st.header("✨ Features")

st.markdown("""
- 📂 Data Explorer
- 🔍 Gene Search
- 📊 Interactive Visualizations
- 🤖 Machine Learning Analysis
- 🧬 Differential Gene Expression Analysis
- 📄 PDF Report Generation
- 📥 CSV Download
""")

st.header("👩‍💻 Developer")

st.success("""
**Soumya Priyadarshini**

BioInsight AI was developed as a bioinformatics project using Streamlit and Python to demonstrate data analysis, visualization, and machine learning techniques.
""")

st.header("🚀 Future Enhancements")

st.markdown("""
- Deep Learning models
- Gene enrichment analysis
- Pathway analysis
- Interactive dashboards
- Cloud database integration
- User authentication
""")

st.markdown("---")
st.caption("© 2026 BioInsight AI | Developed by Soumya Priyadarshini")