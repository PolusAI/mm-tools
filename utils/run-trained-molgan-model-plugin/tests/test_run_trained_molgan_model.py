"""Tests for run_trained_molgan_model."""
import sys
from pathlib import Path

current_dir = Path(__file__).resolve().parent
target_dir = current_dir.parent.parent.parent / "cwl_utils"
sys.path.append(str(target_dir))

from cwl_utilities import call_cwltool  # noqa: E402
from cwl_utilities import create_input_yaml  # noqa: E402
from cwl_utilities import parse_cwl_arguments  # noqa: E402


def test_run_trained_molgan_model() -> None:
    """Test run_trained_molgan_model."""
    cwl_file = Path("run_trained_molgan_model_0.1.0.cwl")

    input_to_props = parse_cwl_arguments(cwl_file)
    input_data_path = "data_30.pkl"
    input_data_path = str(Path(__file__).resolve().parent / Path(input_data_path))
    input_to_props["input_data_path"]["path"] = input_data_path

    input_np_score_path = "NP_score.pkl.gz"
    input_np_score_path = str(
        Path(__file__).resolve().parent / Path(input_np_score_path),
    )
    input_to_props["input_NP_Score_path"]["path"] = input_np_score_path

    input_sa_score_path = "SA_score.pkl.gz"
    input_sa_score_path = str(
        Path(__file__).resolve().parent / Path(input_sa_score_path),
    )
    input_to_props["input_SA_Score_path"]["path"] = input_sa_score_path

    input_model_dir = "trainded_models"
    input_to_props["input_model_dir"] = str(
        Path(__file__).resolve().parent / Path(input_model_dir),
    )
    input_to_props["input_model_dir"] = input_model_dir

    input_to_props["output_sdf_path"] = "generated_mols.sdf"
    input_to_props["validation_metrics"] = "logp"
    input_yaml_path = Path("train_molgan_model.yml")
    create_input_yaml(input_to_props, input_yaml_path)
    call_cwltool(cwl_file, input_yaml_path)

    assert Path("generated_mols.sdf").exists()
