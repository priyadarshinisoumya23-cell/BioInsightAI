import streamlit as st
import pandas as pd
import plotly.express as px

from utils.data_loader import load_data

st.set_page_config(
    page_title="Differential Expression",
    page_icon="🧬",
    layout="wide"
)

st.title("🧬 Differential Gene Expression Analysis")

try:
    # Load dataset
    expression_data = load_data()

    st.success("✅ Dataset Loaded Successfully")

    # -------------------------------------
    # Calculate Mean Gene Expression
    # -------------------------------------
    gene_mean = expression_data.mean(axis=1)

    results = pd.DataFrame({
        "Gene": expression_data.index.astype(str),
        "Mean Expression": gene_mean.values
    })

    # Sort genes by expression
    results = results.sort_values(
        by="Mean Expression",
        ascending=False
    )

    # Display Top 20
    top20 = results.head(20)

    st.subheader("🏆 Top 20 Highly Expressed Genes")
    st.dataframe(top20, use_container_width=True)

    # -------------------------------------
    # Interactive Plotly Bar Chart
    # -------------------------------------
    fig = px.bar(
        top20,
        x="Gene",
        y="Mean Expression",
        color="Mean Expression",
        text="Mean Expression",
        color_continuous_scale="Viridis",
        title="Top 20 Highly Expressed Genes"
    )

    fig.update_traces(
        texttemplate="%{text:.2f}",
        textposition="outside"
    )

    fig.update_layout(
        xaxis_title="Gene ID",
        yaxis_title="Mean Expression",
        xaxis_tickangle=-45,
        template="plotly_white",
        height=600
    )

    st.plotly_chart(fig, use_container_width=True)

    # -------------------------------------
    # Dataset Statistics
    # -------------------------------------
    st.subheader("📊 Dataset Statistics")

    col1, col2, col3 = st.columns(3)

    col1.metric("Genes", expression_data.shape[0])
    col2.metric("Samples", expression_data.shape[1])
    col3.metric(
        "Average Expression",
        f"{gene_mean.mean():.2f}"
    )

    # -------------------------------------
    # Download Results
    # -------------------------------------
    csv = results.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="⬇️ Download Differential Expression Results",
        data=csv,
        file_name="differential_expression_results.csv",
        mime="text/csv"
    )

except Exception as e:
    st.error(f"❌ Error: {e}")