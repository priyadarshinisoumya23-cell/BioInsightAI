import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Report",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Analysis Report")

file_path = "data/raw/GSE45827_series_matrix.txt"

try:
    # Find where the data table starts
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

    st.subheader("Dataset Summary")

    rows, cols = expression_data.shape

    st.write(f"**Number of Genes:** {rows}")
    st.write(f"**Number of Samples:** {cols}")

    st.subheader("Summary Statistics")
    st.dataframe(expression_data.describe())

    csv = expression_data.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="⬇️ Download Cleaned Dataset",
        data=csv,
        file_name="cleaned_gene_expression.csv",
        mime="text/csv"
    )

except Exception as e:
    st.error(f"❌ Error: {e}")