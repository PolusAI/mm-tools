"""Tests for extract_pdbids_drugbank_xsdata."""
from pathlib import Path

from polus.mm.utils.extract_pdbids_drugbank_xsdata.extract_pdbids_drugbank_xsdata import (  # noqa: E501
    extract_pdbids_drugbank_xsdata,
)
from sophios.api.pythonapi import Step
from sophios.api.pythonapi import Workflow


def test_extract_pdbids_drugbank_xsdata() -> None:
    """Test extract_pdbids_drugbank_xsdata."""
    # Fake SMILES
    inchi = ["InChI3491", "InChI8564", "InChI7556"]

    input_xml_path = "drugbank_10_fake_records_5.1.10.xml"

    input_xml_path = str(Path(__file__).resolve().parent / Path(input_xml_path))

    extract_pdbids_drugbank_xsdata(input_xml_path, [], inchi, [], "output.txt")

    assert Path("output.txt").exists()


def test_extract_pdbids_drugbank_xsdata_cwl() -> None:
    """Test extract_pdbids_drugbank_xsdata CWL."""
    cwl_file = Path("extract_pdbids_drugbank_xsdata_0@1@0.cwl")

    # Create the step for the CWL file
    extract_pdbids_drugbank_xsdata_step = Step(clt_path=cwl_file)

    input_xml_path = "drugbank_10_fake_records_5.1.10.xml"
    input_xml_path = str(Path(__file__).resolve().parent / Path(input_xml_path))

    inchi = ["InChI3491", "InChI8564", "InChI7556"]

    extract_pdbids_drugbank_xsdata_step.drugbank_xml_file_path = input_xml_path
    extract_pdbids_drugbank_xsdata_step.inchi = inchi
    extract_pdbids_drugbank_xsdata_step.output_txt_path = "output_cwl.txt"

    # Define the workflow with the step
    steps = [extract_pdbids_drugbank_xsdata_step]
    filename = "extract_pdbids_drugbank_xsdata"
    workflow = Workflow(steps, filename)

    # Run the workflow
    workflow.run()

    # Check for the existence of the output file
    outdir = Path("outdir")
    assert any(
        file.name == "output_cwl.txt" for file in outdir.rglob("*")
    ), "The file output_cwl.txt was not found."
