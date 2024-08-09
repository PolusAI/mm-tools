"""Tests for extract_data_csv."""
from pathlib import Path

from polus.mm.utils.extract_data_csv.extract_data_csv import extract_data_csv


def test_extract_data_csv() -> None:
    """Test extract_data_csv."""
    input_csv_path = "fake_sample_records.csv"
    input_csv_path = str(Path(__file__).resolve().parent / Path(input_csv_path))
    query = ""
    column_name = "Smiles"
    output_txt_path = "smiles.txt"

    extract_data_csv(input_csv_path, query, column_name, output_txt_path)

    assert Path(output_txt_path).exists()
