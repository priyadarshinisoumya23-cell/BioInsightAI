import streamlit as st
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Machine Learning",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Machine Learning Analysis")

file_path = "data/raw/GSE45827_series_matrix.txt"

try:
    # Find the start of the data table
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

    # PCA
    pca = PCA(n_components=2)
    pca_result = pca.fit_transform(expression_data.T)

    # K-Means Clustering
    kmeans = KMeans(n_clusters=3, random_state=42)
    clusters = kmeans.fit_predict(pca_result)

    # Plot
    fig, ax = plt.subplots(figsize=(8, 6))

    scatter = ax.scatter(
        pca_result[:, 0],
        pca_result[:, 1],
        c=clusters,
        cmap="viridis",
        s=60
    )

    ax.set_title("PCA with K-Means Clustering")
    ax.set_xlabel("Principal Component 1")
    ax.set_ylabel("Principal Component 2")

    st.pyplot(fig)

except Exception as e:
    st.error(f"❌ Error: {e}")