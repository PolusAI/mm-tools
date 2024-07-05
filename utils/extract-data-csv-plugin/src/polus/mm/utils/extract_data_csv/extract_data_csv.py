"""Extract data from a CSV file."""
from pathlib import Path

import pandas


def extract_data_csv(  # noqa: PLR0913
    input_csv_path: str,
    query: str,
    column_name: str,
    output_txt_path: str,
    min_row: int = 1,
    max_row: int = -1,
) -> None:
    """extract_data_csv.

    Args:
        input_csv_path: Path to the input csv file, Type string, File type input
        query: query str to search the dataset, Type string, File type input
        column_name: The name of the column to load data, Type string, File type input
        output_txt_path: Path to the txt datoutput file, Type string, File type output
        min_row: The row min inex, Type int
        max_row: The row max inex, Type int
    Returns:
        None
    """
    df = pandas.read_csv(input_csv_path)

    print(df.shape)  # noqa: T201
    print(df.columns)  # noqa: T201g

    if query:
        df = df.query(query)
        print(df)  # noqa: T201

    # Perform row slicing (if any)
    if int(min_row) != 1 or int(max_row) != -1:
        # We want to convert to zero-based indices and we also want
        # the upper index to be inclusive (i.e. <=) so -1 lower index.
        df = df[(int(min_row) - 1) : int(max_row)]
        print(df)  # noqa: T201

    # Now restrict to the column we want
    with Path.open(Path(output_txt_path), mode="w", encoding="utf-8") as f:
        f.write("\n".join(df[column_name].dropna().to_list()))
