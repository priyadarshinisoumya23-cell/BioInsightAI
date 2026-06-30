import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Data Explorer",
    page_icon="📂",
    layout="wide"
)

st.title("📂 Data Explorer")
st.write("Explore the Gene Expression Dataset")

file_path = "data/raw/GSE45827_series_matrix.txt"

try:
    # Find where the expression table begins
    start_line = 0

    with open(file_path, "r") as file:
        for i, line in enumerate(file):
            if line.startswith("!series_matrix_table_begin"):
                start_line = i + 1
                break

    # Read dataset
    df = pd.read_csv(
        file_path,
        sep="\t",
        skiprows=start_line,
        low_memory=False
    )

    # Remove end marker
    df = df[df.iloc[:, 0] != "!series_matrix_table_end"]

    # Clean data
    expression_data = df.iloc[:, 1:]
    expression_data = expression_data.apply(pd.to_numeric, errors="coerce")
    expression_data = expression_data.dropna(axis=1, how="all")
    expression_data = expression_data.fillna(expression_data.mean())

    st.success("✅ Dataset Loaded Successfully")

    st.subheader("Dataset Preview")
    st.dataframe(expression_data.head())

    st.subheader("Dataset Shape")
    rows, cols = expression_data.shape

    col1, col2 = st.columns(2)
    col1.metric("Rows", rows)
    col2.metric("Columns", cols)

    st.subheader("Summary Statistics")
    st.dataframe(expression_data.describe())

except Exception as e:
    st.error(f"❌ Error: {e}")