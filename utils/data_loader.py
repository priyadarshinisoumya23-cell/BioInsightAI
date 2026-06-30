import pandas as pd

def load_data():
    file_path = "data/raw/GSE45827_series_matrix.txt"

    start_line = 0

    with open(file_path, "r") as file:
        for i, line in enumerate(file):
            if line.startswith("!series_matrix_table_begin"):
                start_line = i + 1
                break

    df = pd.read_csv(
        file_path,
        sep="\t",
        skiprows=start_line,
        low_memory=False
    )

    df = df[df.iloc[:, 0] != "!series_matrix_table_end"]

    expression_data = df.iloc[:, 1:]
    expression_data = expression_data.apply(pd.to_numeric, errors="coerce")
    expression_data = expression_data.dropna(axis=1, how="all")
    expression_data = expression_data.fillna(expression_data.mean())

    return expression_data