import streamlit as st
import pandas as pd
from utils.data_loader import load_data

# ----------------------------------------------------
# Page Configuration
# ----------------------------------------------------
st.set_page_config(
    page_title="Data Explorer",
    page_icon="📂",
    layout="wide"
)

st.title("📂 Data Explorer")
st.markdown("Explore the gene expression dataset and search for specific Gene IDs.")

try:
    # ----------------------------------------------------
    # Load Dataset
    # ----------------------------------------------------
    expression_data = load_data()
    st.write(expression_data.index[:10].tolist())

    st.success("✅ Dataset Loaded Successfully!")

    # Make sure index is string
    expression_data.index = expression_data.index.astype(str).str.strip()

    # ----------------------------------------------------
    # Metrics
    # ----------------------------------------------------
    rows, cols = expression_data.shape

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("🧬 Total Genes", rows)

    with col2:
        st.metric("🧪 Total Samples", cols)

    with col3:
        st.metric(
            "📊 Average Expression",
            f"{expression_data.mean().mean():.2f}"
        )

    st.divider()

    # ----------------------------------------------------
    # First 20 Gene IDs
    # ----------------------------------------------------
    st.subheader("🧬 First 20 Gene IDs")

    gene_df = pd.DataFrame({
        "Gene ID": expression_data.index[:20]
    })

    st.dataframe(gene_df, use_container_width=True)

    st.divider()

    # ----------------------------------------------------
    # Gene Search
    # ----------------------------------------------------
    st.subheader("🔍 Search Gene")

    gene = st.text_input(
        "Enter Gene ID",
        placeholder="Example: 1007_s_at"
    )

    if gene:

        gene = gene.strip()

        # Exact match
        if gene in expression_data.index:

            st.success(f"✅ Gene '{gene}' Found!")

            st.dataframe(
                expression_data.loc[[gene]],
                use_container_width=True
            )

        else:

            # Partial search
            matches = expression_data.index[
                expression_data.index.str.contains(
                    gene,
                    case=False,
                    na=False
                )
            ]

            if len(matches) > 0:

                st.info(f"Found {len(matches)} matching Gene IDs")

                selected_gene = st.selectbox(
                    "Select Gene",
                    matches
                )

                st.dataframe(
                    expression_data.loc[[selected_gene]],
                    use_container_width=True
                )

            else:
                st.error("❌ Gene ID not found.")

    st.divider()

    # ----------------------------------------------------
    # Dataset Preview
    # ----------------------------------------------------
    st.subheader("📋 Dataset Preview")

    st.dataframe(
        expression_data.head(20),
        use_container_width=True
    )

    st.divider()

    # ----------------------------------------------------
    # Summary Statistics
    # ----------------------------------------------------
    st.subheader("📈 Summary Statistics")

    st.dataframe(
        expression_data.describe(),
        use_container_width=True
    )

    st.divider()

    # ----------------------------------------------------
    # Download Dataset
    # ----------------------------------------------------
    csv = expression_data.to_csv().encode("utf-8")

    st.download_button(
        label="⬇️ Download Dataset (CSV)",
        data=csv,
        file_name="gene_expression_dataset.csv",
        mime="text/csv"
    )

except Exception as e:
    st.error(f"❌ Error: {e}")