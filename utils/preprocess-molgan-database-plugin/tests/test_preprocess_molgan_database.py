"""Tests for preprocess_molgan_database."""
import sys
from pathlib import Path

current_dir = Path(__file__).resolve().parent
target_dir = current_dir.parent.parent.parent / "cwl_utils"
sys.path.append(str(target_dir))

from cwl_utilities import call_cwltool  # noqa: E402
from cwl_utilities import create_input_yaml  # noqa: E402
from cwl_utilities import parse_cwl_arguments  # noqa: E402


def test_preprocess_molgan_database() -> None:
    """Test preprocess_molgan_database."""
    cwl_file = Path("preprocess_molgan_database_0.1.0.cwl")
    input_to_props = parse_cwl_arguments(cwl_file)
    file_path_str = "gdb9_5.sdf"
    file_path = str(Path(__file__).resolve().parent / Path(file_path_str))
    input_to_props["input_sdf_path"]["path"] = file_path
    input_yaml_path = Path("preprocess_molgan_database_0.1.0.yml")

    create_input_yaml(input_to_props, input_yaml_path)
    call_cwltool(cwl_file, input_yaml_path)
    assert Path("system.pkl").exists()
