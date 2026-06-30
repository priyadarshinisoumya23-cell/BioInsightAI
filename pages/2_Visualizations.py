import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Visualizations",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Data Visualizations")

file_path = "data/raw/GSE45827_series_matrix.txt"

try:
    # Find the beginning of the data table
    start_line = 0
    with open(file_path, "r") as file:
        for i, line in enumerate(file):
            if line.startswith("!series_matrix_table_begin"):
                start_line = i + 1
                break

    # Read the dataset
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

    # Heatmap
    st.subheader("🔥 Correlation Heatmap")
    corr = expression_data.iloc[:, :30].corr()

    fig1, ax1 = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr, cmap="coolwarm", ax=ax1)
    st.pyplot(fig1)

    # Box Plot
    st.subheader("📦 Box Plot")

    fig2, ax2 = plt.subplots(figsize=(12, 6))
    expression_data.iloc[:, :10].boxplot(ax=ax2)
    plt.xticks(rotation=45)
    st.pyplot(fig2)

    # Violin Plot
    st.subheader("🎻 Violin Plot")

    fig3, ax3 = plt.subplots(figsize=(12, 6))
    sns.violinplot(data=expression_data.iloc[:, :10], ax=ax3)
    plt.xticks(rotation=45)
    st.pyplot(fig3)

except Exception as e:
    st.error(f"Error: {e}")