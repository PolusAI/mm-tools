"""Tests for load_trained_molgan_model."""
from pathlib import Path

from sophios.api.pythonapi import Step
from sophios.api.pythonapi import Workflow


def test_load_trained_molgan_model_cwl() -> None:
    """Test load_trained_molgan_model CWL."""
    cwl_file = Path("load_trained_molgan_model_0@1@0.cwl")

    # Create the step for the CWL file
    load_trained_molgan_model_step = Step(clt_path=cwl_file)

    load_trained_molgan_model_step.input_data_path = "/MolGAN/data/data.pkl"
    load_trained_molgan_model_step.input_NP_Score_path = "/MolGAN/data/NP_score.pkl.gz"
    load_trained_molgan_model_step.input_SA_Score_path = "/MolGAN/data/SA_score.pkl.gz"
    load_trained_molgan_model_step.input_model_dir = "/MolGAN/trained_models"
    load_trained_molgan_model_step.output_sdf_path = "generated_mols.sdf"
    load_trained_molgan_model_step.output_log_path = "output.txt"

    # Define the workflow with the step
    steps = [load_trained_molgan_model_step]
    filename = "load_trained_molgan_model"
    workflow = Workflow(steps, filename)

    # Run the workflow
    workflow.run()

    # Check for the existence of the output file
    outdir = Path("outdir")
    assert any(
        file.name == "generated_mols.sdf" for file in outdir.rglob("*")
    ), "The file generated_mols.sdf was not found."
