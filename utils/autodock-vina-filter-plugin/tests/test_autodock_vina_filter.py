"""Tests for autodock_vina_filter."""
from pathlib import Path

from sophios.api.pythonapi import Step
from sophios.api.pythonapi import Workflow

# def test_autodock_vina_filter() -> None:
#     """Test autodock_vina_filter."""

#     autodock_vina_filter(
#         input_log_path,
#         input_log_paths,
#         docking_score_cutoff,
#         max_num_poses_per_ligand,
#         max_num_poses_total,
#         input_txt_path,
#         rescore,


def test_cwl_autodock_vina_filter() -> None:
    """Test autodock_vina_filter in cwltool."""
    cwl_file = Path("autodock_vina_filter_0@1@0.cwl")

    # Create the step for the CWL file
    autodock_vina_filter_step = Step(clt_path=cwl_file)

    input_log_path = "vina.log"
    input_log_path = str(Path(__file__).resolve().parent / Path(input_log_path))
    autodock_vina_filter_step.input_log_path = input_log_path

    autodock_vina_filter_step.input_log_paths = []  # None
    input_txt_path = "binding_data.txt"
    input_txt_path = str(Path(__file__).resolve().parent / Path(input_txt_path))

    autodock_vina_filter_step.input_txt_path = input_txt_path

    input_ligand_pdbqt_path = "1e3g.pdqt"
    input_ligand_pdbqt_path = str(
        Path(__file__).resolve().parent / Path(input_ligand_pdbqt_path),
    )
    autodock_vina_filter_step.input_ligand_pdbqt_path = [input_ligand_pdbqt_path]

    input_receptor_pdbqt_path = "1e3g_protein.pdb"
    input_receptor_pdbqt_path = str(
        Path(__file__).resolve().parent / Path(input_receptor_pdbqt_path),
    )
    autodock_vina_filter_step.input_receptor_pdbqt_path = [input_receptor_pdbqt_path]

    autodock_vina_filter_step.docking_score_cutoff = -1.0
    autodock_vina_filter_step.max_num_poses_per_ligand = 1
    autodock_vina_filter_step.max_num_poses_total = 1
    autodock_vina_filter_step.rescore = True
    autodock_vina_filter_step.output_receptor_pdbqt_path = "./"
    autodock_vina_filter_step.output_ligand_pdbqt_path = "./"

    # Define the workflow with the step
    steps = [autodock_vina_filter_step]
    filename = "autodock_vina_filter"
    workflow = Workflow(steps, filename)

    # Run the workflow
    workflow.run()

    # Check for the existence of the output file
    outdir = Path("outdir")
    assert any(
        file.name == "indices.txt" for file in outdir.rglob("*")
    ), "The file indices.txt was not found."
