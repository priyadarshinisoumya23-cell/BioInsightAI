import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="BioInsight AI",
    page_icon="🧬",
    layout="wide"
)

st.title("🧬 BioInsight AI")
st.subheader("Gene Expression Analysis Dashboard")

# --------------------------------------------------
# Dataset Path
# --------------------------------------------------
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

    st.success("✅ Dataset Loaded Successfully!")

    # --------------------------------------------------
    # Data Cleaning
    # --------------------------------------------------
    expression_data = df.iloc[:, 1:]

    expression_data = expression_data.apply(
        pd.to_numeric,
        errors="coerce"
    )

    expression_data = expression_data.dropna(
        axis=1,
        how="all"
    )

    expression_data = expression_data.fillna(
        expression_data.mean()
    )

    # --------------------------------------------------
    # Dataset Preview
    # --------------------------------------------------
    st.header("📄 Cleaned Dataset")
    st.dataframe(expression_data.head())

    # --------------------------------------------------
    # Dataset Shape
    # --------------------------------------------------
    st.header("📏 Dataset Shape")
    st.write(expression_data.shape)

    # --------------------------------------------------
    # Correlation Heatmap
    # --------------------------------------------------
    st.header("🔥 Correlation Heatmap")

    corr = expression_data.iloc[:, :30].corr()

    fig1, ax1 = plt.subplots(figsize=(10, 8))

    sns.heatmap(
        corr,
        cmap="coolwarm",
        ax=ax1
    )

    st.pyplot(fig1)

    # --------------------------------------------------
    # Box Plot
    # --------------------------------------------------
    st.header("📦 Box Plot")

    fig2, ax2 = plt.subplots(figsize=(12, 6))

    expression_data.iloc[:, :10].boxplot(ax=ax2)

    plt.xticks(rotation=45)

    st.pyplot(fig2)

    # --------------------------------------------------
    # Violin Plot
    # --------------------------------------------------
    st.header("🎻 Violin Plot")

    fig3, ax3 = plt.subplots(figsize=(12, 6))

    sns.violinplot(
        data=expression_data.iloc[:, :10],
        ax=ax3
    )

    plt.xticks(rotation=45)

    st.pyplot(fig3)

    # --------------------------------------------------
    # Summary Statistics
    # --------------------------------------------------
    st.header("📊 Summary Statistics")

    st.dataframe(expression_data.describe())

    # --------------------------------------------------
    # PCA Visualization
    # --------------------------------------------------
    st.header("📈 PCA Visualization")

    # Samples become rows
    pca_data = expression_data.T

    pca = PCA(n_components=2)

    pca_result = pca.fit_transform(pca_data)

    pca_df = pd.DataFrame(
        pca_result,
        columns=["PC1", "PC2"]
    )

    fig4, ax4 = plt.subplots(figsize=(8, 6))

    ax4.scatter(
        pca_df["PC1"],
        pca_df["PC2"],
        color="blue"
    )

    ax4.set_xlabel("Principal Component 1")
    ax4.set_ylabel("Principal Component 2")
    ax4.set_title("PCA of Gene Expression Data")

    st.pyplot(fig4)

except Exception as e:
    st.error(f"❌ Error: {e}")