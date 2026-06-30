import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestClassifier

from utils.data_loader import load_data

st.set_page_config(
    page_title="Machine Learning",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Machine Learning Analysis")

try:
    # Load data
    expression_data = load_data()

    # PCA
    pca = PCA(n_components=2)
    pca_result = pca.fit_transform(expression_data.T)

    # Dummy labels (for demonstration)
    labels = [0] * (len(pca_result) // 2) + [1] * (len(pca_result) - len(pca_result) // 2)

    # Random Forest
    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    model.fit(pca_result, labels)

    accuracy = model.score(pca_result, labels)

    # Show accuracy
    st.subheader("🎯 Model Accuracy")
    st.metric("Accuracy", f"{accuracy * 100:.2f}%")

    # K-Means
    kmeans = KMeans(
        n_clusters=3,
        random_state=42,
        n_init=10
    )

    clusters = kmeans.fit_predict(pca_result)

    # PCA Plot
    st.subheader("📊 PCA + K-Means Clustering")

    fig, ax = plt.subplots(figsize=(8, 6))

    scatter = ax.scatter(
        pca_result[:, 0],
        pca_result[:, 1],
        c=clusters,
        cmap="viridis",
        s=70
    )

    ax.set_xlabel("Principal Component 1")
    ax.set_ylabel("Principal Component 2")
    ax.set_title("PCA + K-Means Clustering")

    plt.colorbar(scatter)

    st.pyplot(fig)

    # Feature Importance
    st.subheader("⭐ Feature Importance")

    importance = pd.DataFrame({
        "Feature": ["PC1", "PC2"],
        "Importance": model.feature_importances_
    })

    st.dataframe(importance)

except Exception as e:
    st.error(f"❌ Error: {e}")