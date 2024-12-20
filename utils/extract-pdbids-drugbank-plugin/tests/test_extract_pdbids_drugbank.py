"""Tests for extract_pdbids_drugbank."""
from pathlib import Path

from polus.mm.utils.extract_pdbids_drugbank.extract_pdbids_drugbank import (
    extract_pdbids_drugbank,
)
from sophios.api.pythonapi import Step
from sophios.api.pythonapi import Workflow


def test_extract_pdbids_drugbank() -> None:
    """Test extract_pdbids_drugbank."""
    # Fake SMILES
    inchi = ["InChI3491", "InChI8564", "InChI7556"]

    input_xml_path = "drugbank_10_fake_records_5.1.10.xml"
    input_xml_path = str(Path(__file__).resolve().parent / Path(input_xml_path))

    extract_pdbids_drugbank(input_xml_path, [], inchi, [], "out.txt")

    assert Path("out.txt").exists()


def test_extract_pdbids_drugbank_cwl() -> None:
    """Test extract_pdbids_drugbank CWL."""
    cwl_file = Path("extract_pdbids_drugbank_0@1@0.cwl")

    # Create the step for the CWL file
    extract_pdbids_drugbank__step = Step(clt_path=cwl_file)

    input_xml_path = "drugbank_10_fake_records_5.1.10.xml"
    input_xml_path = str(Path(__file__).resolve().parent / Path(input_xml_path))

    inchi = ["InChI3491", "InChI8564", "InChI7556"]

    extract_pdbids_drugbank__step.drugbank_xml_file_path = input_xml_path
    extract_pdbids_drugbank__step.inchi = inchi
    extract_pdbids_drugbank__step.output_txt_path = "output_cwl.txt"

    # Define the workflow with the step
    steps = [extract_pdbids_drugbank__step]
    filename = "extract_pdbids_drugbank_"
    workflow = Workflow(steps, filename)

    # Run the workflow
    workflow.run()

    # Check for the existence of the output file
    outdir = Path("outdir")
    assert any(
        file.name == "output_cwl.txt" for file in outdir.rglob("*")
    ), "The file output_cwl.txt was not found."
