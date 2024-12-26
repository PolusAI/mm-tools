"""Tests for autodock_vina_rescore."""
from pathlib import Path

from sophios.api.pythonapi import Step
from sophios.api.pythonapi import Workflow


def test_autodock_vina_rescore_cwl() -> None:
    """Test autodock_vina_rescore CWL."""
    cwl_file = Path("autodock_vina_rescore_0@1@0.cwl")

    autodock_vina_rescore_step = Step(clt_path=cwl_file)

    ligand_path = "ligand.pdbqt"
    ligand_path = str(Path(__file__).resolve().parent / Path(ligand_path))
    receptor_path = "receptor.pdbqt"
    receptor_path = str(Path(__file__).resolve().parent / Path(receptor_path))

    autodock_vina_rescore_step.input_ligand_pdbqt_path = ligand_path
    autodock_vina_rescore_step.input_receptor_pdbqt_path = receptor_path
    autodock_vina_rescore_step.score_only = True
    autodock_vina_rescore_step.output_log_path = "vina_rescore_pdbind.log"

    steps = [autodock_vina_rescore_step]
    filename = "autodock_vina_rescore"
    viz = Workflow(steps, filename)

    viz.run()

    # Check for the existence of the output file
    outdir = Path("outdir")
    assert any(
        file.name == "autodock_vina_rescore" for file in outdir.rglob("*")
    ), "The file autodock_vina_rescore was not found."
