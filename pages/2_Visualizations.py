import streamlit as st
import plotly.express as px
from utils.data_loader import load_data

st.set_page_config(
    page_title="Visualizations",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Interactive Visualizations")

try:
    expression_data = load_data()

    st.success("✅ Dataset Loaded Successfully")

    # -----------------------------
    # Box Plot
    # -----------------------------
    st.subheader("📦 Gene Expression Box Plot")

    fig_box = px.box(
        expression_data.iloc[:, :10],
        points=False
    )

    st.plotly_chart(fig_box, use_container_width=True)

    # -----------------------------
    # Violin Plot
    # -----------------------------
    st.subheader("🎻 Gene Expression Violin Plot")

    fig_violin = px.violin(
        expression_data.iloc[:, :10]
    )

    st.plotly_chart(fig_violin, use_container_width=True)

except Exception as e:
    st.error(f"❌ Error: {e}")