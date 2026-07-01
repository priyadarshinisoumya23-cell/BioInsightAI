import pandas as pd
import streamlit as st


@st.cache_data
def load_data():
    file_path = "data/raw/GSE45827_series_matrix.txt"

    # Find the start of the expression table
    start_line = None

    with open(file_path, "r", encoding="utf-8") as f:
        for i, line in enumerate(f):
            if "!series_matrix_table_begin" in line:
                start_line = i + 1
                break

    if start_line is None:
        raise Exception("Expression table not found!")

    # Read the expression matrix
    df = pd.read_csv(
        file_path,
        sep="\t",
        skiprows=start_line,
        header=0,
        quotechar='"',
        engine="python",
       
    )

    # Remove GEO end marker
    df = df[df.iloc[:, 0] != "!series_matrix_table_end"]

    # Clean column names
    df.columns = (
        df.columns.astype(str)
        .str.replace('"', '', regex=False)
        .str.strip()
    )

    # Clean first column (Gene IDs)
    df.iloc[:, 0] = (
        df.iloc[:, 0]
        .astype(str)
        .str.replace('"', '', regex=False)
        .str.strip()
    )

    # Rename first column to ID_REF
    df.rename(columns={df.columns[0]: "ID_REF"}, inplace=True)

    # Remove duplicate Gene IDs
    df.drop_duplicates(subset="ID_REF", inplace=True)

    # Set ID_REF as index
    df.set_index("ID_REF", inplace=True)

    # Convert expression values to numeric
    df = df.apply(pd.to_numeric, errors="coerce")

    # Remove completely empty rows and columns
    df.dropna(axis=0, how="all", inplace=True)
    df.dropna(axis=1, how="all", inplace=True)

    # Fill missing values with column mean
    df = df.fillna(df.mean(numeric_only=True))

    # Clean index
    df.index = (
        df.index.astype(str)
        .str.replace('"', '', regex=False)
        .str.strip()
    )

    return df