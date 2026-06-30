import pandas as pd
import streamlit as st


@st.cache_data
def load_data():
    file_path = "data/raw/GSE45827_series_matrix.txt"

    # Find where the expression table starts
    start_line = 0

    with open(file_path, "r") as file:
        for i, line in enumerate(file):
            if line.startswith("!series_matrix_table_begin"):
                start_line = i + 1
                break

    # Read expression matrix
    df = pd.read_csv(
        file_path,
        sep="\t",
        skiprows=start_line,
        low_memory=False
    )

    # Remove end marker
    df = df[df.iloc[:, 0] != "!series_matrix_table_end"]

    # Rename first column
    df.rename(columns={df.columns[0]: "Gene_ID"}, inplace=True)

    # Set Gene_ID as index
    df.set_index("Gene_ID", inplace=True)

    # Convert all values to numeric
    df = df.apply(pd.to_numeric, errors="coerce")

    # Remove empty rows and columns
    df.dropna(axis=0, how="all", inplace=True)
    df.dropna(axis=1, how="all", inplace=True)

    # Fill missing values
    df.fillna(df.mean(), inplace=True)

    # Convert Gene IDs to string
    df.index = df.index.astype(str)

    return df