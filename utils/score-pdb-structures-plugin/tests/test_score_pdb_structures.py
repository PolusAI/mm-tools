"""Tests for score_pdb_structures."""
from pathlib import Path

from polus.mm.utils.score_pdb_structures.score_pdb_structures import (
    score_pdb_structures,
)
from sophios.api.pythonapi import Step
from sophios.api.pythonapi import Workflow


def test_score_pdb_structures() -> None:
    """Test score_pdb_structures."""
    input_pdbids = [
        "1g0i",
        "1iev",
        "1ptg",
        "1y7v",
        "2huo",
        "2os9",
        "2r71",
        "2x1i",
        "3bxd",
        "1aod",
    ]
    score_pdb_structures(input_pdbids, "output.txt", max_row=1)

    assert Path("output.txt").exists()


def test_score_pdb_structures_cwl() -> None:
    """Test score_pdb_structures CWL."""
    cwl_file = Path("score_pdb_structures_0@1@0.cwl")

    # Create the step for the CWL file
    score_pdb_structures_step = Step(clt_path=cwl_file)
    input_pdbids = [
        "1g0i",
        "1iev",
        "1ptg",
        "1y7v",
        "2huo",
        "2os9",
        "2r71",
        "2x1i",
        "3bxd",
        "1aod",
    ]

    score_pdb_structures_step.input_pdbids = input_pdbids
    score_pdb_structures_step.output_txt_path = "output_scored.txt"
    score_pdb_structures_step.max_row = 1

    # Define the workflow with the step
    steps = [score_pdb_structures_step]
    filename = "score_pdb_structures"
    workflow = Workflow(steps, filename)

    # Run the workflow
    workflow.run()

    # Check for the existence of the output file
    outdir = Path("outdir")
    assert any(
        file.name == "output_scored.txt" for file in outdir.rglob("*")
    ), "The file output_scored.txt was not found."
