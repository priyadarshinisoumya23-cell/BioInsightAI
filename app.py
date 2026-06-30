import streamlit as st

st.set_page_config(
    page_title="BioInsight AI",
    page_icon="🧬",
    layout="wide"
)

st.title("🧬 BioInsight AI")
st.subheader("Gene Expression Analysis Dashboard")

st.markdown("""
## Welcome!

This application provides:

- 📂 Data Explorer
- 📊 Visualizations
- 🤖 Machine Learning
- 📄 Report Generation

Use the **sidebar** to navigate between pages.
""")

st.info("👈 Select a page from the sidebar to begin.")