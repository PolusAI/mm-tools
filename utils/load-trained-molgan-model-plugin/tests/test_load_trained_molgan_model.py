"""Tests for load_trained_molgan_model."""
import sys
from pathlib import Path

current_dir = Path(__file__).resolve().parent
target_dir = current_dir.parent.parent.parent / "cwl_utils"
sys.path.append(str(target_dir))

from cwl_utilities import call_cwltool  # noqa: E402
from cwl_utilities import create_input_yaml  # noqa: E402
from cwl_utilities import parse_cwl_arguments  # noqa: E402


def test_load_trained_molgan_model() -> None:
    """Test load_trained_molgan_model."""
    cwl_file = Path("load_trained_molgan_model_0.1.0.cwl")

    input_to_props = parse_cwl_arguments(cwl_file)

    input_to_props["input_data_path"] = "/MolGAN/data/data.pkl"

    input_to_props["input_NP_Score_path"] = "/MolGAN/data/NP_score.pkl.gz"

    input_to_props["input_SA_Score_path"] = "/MolGAN/data/SA_score.pkl.gz"

    input_to_props["input_model_dir"] = "/MolGAN/trained_models"

    input_to_props["output_sdf_path"] = "generated_mols.sdf"

    input_yaml_path = Path("load_trained_molgan_model_0.1.0.yml")
    create_input_yaml(input_to_props, input_yaml_path)
    call_cwltool(cwl_file, input_yaml_path)
    assert Path("generated_mols.sdf").exists()