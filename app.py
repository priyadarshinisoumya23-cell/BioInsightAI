import streamlit as st

st.set_page_config(
    page_title="BioInsight AI",
    page_icon="🧬",
    layout="wide"
)

st.title("🧬 BioInsight AI")
st.subheader("Gene Expression Analysis Dashboard")

st.markdown("---")

st.markdown("""
## Welcome to BioInsight AI

BioInsight AI is a bioinformatics dashboard for exploring and analyzing gene expression datasets.

### Features

- 📂 Data Explorer
- 📊 Interactive Visualizations
- 🤖 Machine Learning Analysis
- 📄 Analysis Report

Use the **sidebar** to navigate through the application.
""")

st.info("👈 Select a page from the sidebar to begin.")