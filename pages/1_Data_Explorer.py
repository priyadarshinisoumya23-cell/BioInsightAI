import streamlit as st
from utils.data_loader import load_data

st.set_page_config(
    page_title="Data Explorer",
    page_icon="📂",
    layout="wide"
)

st.title("📂 Data Explorer")

try:
    expression_data = load_data()

    st.success("✅ Dataset Loaded Successfully")

    # Metrics
    rows, cols = expression_data.shape

    col1, col2 = st.columns(2)

    col1.metric("Genes", rows)
    col2.metric("Samples", cols)

    st.divider()

    # Search
    st.subheader("🔍 Search Gene")

    gene = st.text_input("Enter Gene ID")

    if gene:
        if gene in expression_data.index:
            st.success("✅ Gene Found")
            st.dataframe(expression_data.loc[[gene]])
        else:
            st.warning("Gene not found")

    st.divider()

    st.subheader("Dataset Preview")
    st.dataframe(expression_data.head(20))

    st.subheader("Summary Statistics")
    st.dataframe(expression_data.describe())

except Exception as e:
    st.error(f"❌ {e}")