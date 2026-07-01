import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from utils.data_loader import load_data

st.set_page_config(
    page_title="Visualizations",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Gene Expression Visualizations")

# Load data
expression_data = load_data()

st.success("Dataset Loaded Successfully")

# Keep only numeric values
expression_data = expression_data.select_dtypes(include="number")

st.subheader("🔥 Correlation Heatmap")

# Use only the first 30 samples to keep the plot manageable
corr = expression_data.iloc[:, :30].corr()

fig, ax = plt.subplots(figsize=(12, 10))

sns.heatmap(
    corr,
    cmap="viridis",
    annot=False,
    square=True,
    ax=ax
)

st.pyplot(fig)

st.divider()

st.subheader("📦 Box Plot")

fig2, ax2 = plt.subplots(figsize=(12, 5))
sns.boxplot(data=expression_data.iloc[:, :10], ax=ax2)
plt.xticks(rotation=90)

st.pyplot(fig2)

st.divider()

st.subheader("🎻 Violin Plot")

fig3, ax3 = plt.subplots(figsize=(12, 5))
sns.violinplot(data=expression_data.iloc[:, :10], ax=ax3)
plt.xticks(rotation=90)

st.pyplot(fig3)