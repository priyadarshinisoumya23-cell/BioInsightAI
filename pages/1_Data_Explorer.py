import streamlit as st
from utils.data_loader import load_data

# -------------------------------------
# Page Configuration
# -------------------------------------
st.set_page_config(
    page_title="Data Explorer",
    page_icon="📂",
    layout="wide"
)

st.title("📂 Data Explorer")
st.write("Explore and analyze the gene expression dataset.")

try:
    # Load Data
    expression_data = load_data()
    st.subheader("First 20 Gene IDs")
    st.write(expression_data.index[:20].tolist())

    # Convert index to string
    expression_data.index = expression_data.index.astype(str)

    st.success("✅ Dataset Loaded Successfully!")

    # -------------------------------------
    # Dashboard Metrics
    # -------------------------------------
    rows, cols = expression_data.shape

    col1, col2, col3 = st.columns(3)

    col1.metric("🧬 Total Genes", rows)
    col2.metric("🧪 Total Samples", cols)
    col3.metric("📊 Average Expression", f"{expression_data.mean().mean():.2f}")

    st.divider()

    # -------------------------------------
    # Gene Search
    # -------------------------------------
    st.subheader("🔍 Search Gene")

    gene = st.text_input(
        "Enter Gene ID",
        placeholder="Type part or full Gene ID..."
    )

    if gene:

        # Find partial matches (case-insensitive)
        matches = expression_data.index[
            expression_data.index.str.contains(
                gene,
                case=False,
                na=False
            )
        ]

        if len(matches) > 0:

            st.success(f"✅ {len(matches)} Gene(s) Found")

            selected_gene = st.selectbox(
                "Select Gene",
                matches
            )

            st.dataframe(
                expression_data.loc[[selected_gene]],
                use_container_width=True
            )

        else:
            st.error("❌ Gene not found.")

    st.divider()

    # -------------------------------------
    # Show First 20 Gene IDs
    # -------------------------------------
    st.subheader("🧬 First 20 Gene IDs")

    gene_df = {"Gene ID": expression_data.index[:20]}
    st.table(gene_df)

    st.divider()

    # -------------------------------------
    # Dataset Preview
    # -------------------------------------
    st.subheader("📋 Dataset Preview")

    st.dataframe(
        expression_data.head(20),
        use_container_width=True
    )

    st.divider()

    # -------------------------------------
    # Summary Statistics
    # -------------------------------------
    st.subheader("📈 Summary Statistics")

    st.dataframe(
        expression_data.describe(),
        use_container_width=True
    )

    st.divider()

    # -------------------------------------
    # Download Dataset
    # -------------------------------------
    csv = expression_data.to_csv().encode("utf-8")

    st.download_button(
        label="⬇️ Download Cleaned Dataset (CSV)",
        data=csv,
        file_name="cleaned_gene_expression.csv",
        mime="text/csv"
    )

except Exception as e:
    st.error(f"❌ Error: {e}")