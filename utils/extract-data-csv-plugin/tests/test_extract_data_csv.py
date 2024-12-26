"""Tests for extract_data_csv."""
from pathlib import Path

from polus.mm.utils.extract_data_csv.extract_data_csv import extract_data_csv
from sophios.api.pythonapi import Step
from sophios.api.pythonapi import Workflow


def test_extract_data_csv() -> None:
    """Test extract_data_csv."""
    input_csv_path = "fake_sample_records.csv"
    input_csv_path = str(Path(__file__).resolve().parent / Path(input_csv_path))
    query = ""
    column_name = "Smiles"
    output_txt_path = "smiles.txt"

    extract_data_csv(input_csv_path, query, column_name, output_txt_path)

    assert Path(output_txt_path).exists()


def test_extract_data_csv_cwl() -> None:
    """Test extract_data_csv CWL."""
    cwl_file = Path("extract_data_csv_0@1@0.cwl")

    # Create the step for the CWL file
    extract_data_csv_step = Step(clt_path=cwl_file)

    input_csv_path = "fake_sample_records.csv"
    input_csv_path = str(Path(__file__).resolve().parent / Path(input_csv_path))

    extract_data_csv_step.input_csv_path = input_csv_path
    extract_data_csv_step.query = ""
    extract_data_csv_step.column_name = "Smiles"
    extract_data_csv_step.output_txt_path = "smiles.txt"

    # Define the workflow with the step
    steps = [extract_data_csv_step]
    filename = "extract_data_csv"
    workflow = Workflow(steps, filename)

    # Run the workflow
    workflow.run()

    # Check for the existence of the output file
    outdir = Path("outdir")
    assert any(
        file.name == "smiles.txt" for file in outdir.rglob("*")
    ), "The file output_scored.txt was not found."
