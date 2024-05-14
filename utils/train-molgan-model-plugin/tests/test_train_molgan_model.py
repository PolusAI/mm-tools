"""Tests for train_molgan_model."""
import sys
from pathlib import Path

current_dir = Path(__file__).resolve().parent
target_dir = current_dir.parent.parent.parent / "cwl_utils"
sys.path.append(str(target_dir))

from cwl_utilities import call_cwltool  # noqa: E402
from cwl_utilities import create_input_yaml  # noqa: E402
from cwl_utilities import parse_cwl_arguments  # noqa: E402


def test_train_molgan_model() -> None:
    """Test train_molgan_model."""
    cwl_file = Path("train_molgan_model.cwl")
    input_to_props = parse_cwl_arguments(cwl_file)
    file_path_str = "ref_output_model_support_vector_machine.pkl"
    file_path = str(Path(__file__).resolve().parent / Path(file_path_str))
    input_to_props["input_data_path"]["path"] = file_path
    file_path_str = "sander.ceout.gz"
    file_path = str(Path(__file__).resolve().parent / Path(file_path_str))
    input_to_props["input_NP_Score_path"]["path"] = file_path
    input_to_props["input_SA_Score_path"]["path"] = file_path
    input_yaml_path = Path("train_molgan_model.yml")
    create_input_yaml(input_to_props, input_yaml_path)
    call_cwltool(cwl_file, input_yaml_path)
    assert Path("system.pkl").exists()
