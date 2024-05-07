"""Tests for mdrun."""
import sys
from pathlib import Path

current_dir = Path(__file__).resolve().parent
target_dir = current_dir.parent.parent.parent / "cwl_utils"
sys.path.append(str(target_dir))

from cwl_utilities import call_cwltool  # noqa: E402
from cwl_utilities import create_input_yaml  # noqa: E402
from cwl_utilities import parse_cwl_arguments  # noqa: E402


def test_mdrun() -> None:
    """Test mdrun."""
    cwl_file_str = "mdrun.cwl"
    cwl_file = Path(__file__).resolve().parent.parent / Path(cwl_file_str)
    input_to_props = parse_cwl_arguments(cwl_file)
    file_path_str = "mdrun.tpr"
    file_path = str(Path(__file__).resolve().parent / Path(file_path_str))
    input_to_props["input_tpr_path"]["path"] = file_path
    del input_to_props["input_cpt_path"]

    input_yaml_path = Path("mdrun.yml")
    create_input_yaml(input_to_props, input_yaml_path)

    stdout, stderr = call_cwltool(cwl_file, input_yaml_path)

    assert Path("system.trr").exists()
