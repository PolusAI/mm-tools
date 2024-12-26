"""Tests for pymol_align_protein_ca."""
from pathlib import Path

from sophios.api.pythonapi import Step
from sophios.api.pythonapi import Workflow


def test_pymol_align_protein_ca_cwl() -> None:
    """Test pymol_align_protein_ca CWL."""
    cwl_file = Path("pymol_align_protein_ca_0@1@0.cwl")

    # Create the step for the CWL file
    load_pymol_align_protein_ca_step = Step(clt_path=cwl_file)

    input_1_path = str(Path(__file__).resolve().parent / Path("receptor.xyz"))
    input_2_path = str(Path(__file__).resolve().parent / Path("pose_ligand.xyz"))
    input_3_path = str(Path(__file__).resolve().parent / Path("npt.gro"))
    input_4_path = str(Path(__file__).resolve().parent / Path("prod.trr"))

    load_pymol_align_protein_ca_step.input_1_path = input_1_path
    load_pymol_align_protein_ca_step.input_2_path = input_2_path
    load_pymol_align_protein_ca_step.input_3_path = input_3_path
    load_pymol_align_protein_ca_step.input_4_path = input_4_path
    load_pymol_align_protein_ca_step.output_file_path = "prod_align_protein_ca.pdb"

    # Define the workflow with the step
    steps = [load_pymol_align_protein_ca_step]
    filename = "pymol_align_protein_ca"
    workflow = Workflow(steps, filename)

    # Run the workflow
    workflow.run()

    # Check for the existence of the output file
    outdir = Path("outdir")
    assert any(
        file.name == "prod_align_protein_ca.pdb" for file in outdir.rglob("*")
    ), "The file prod_align_protein_ca.pdb was not found."
