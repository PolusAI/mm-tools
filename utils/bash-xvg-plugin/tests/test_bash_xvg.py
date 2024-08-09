"""Tests for bash_xvg."""
import sys
from pathlib import Path

current_dir = Path(__file__).resolve().parent
target_dir = current_dir.parent.parent.parent / "cwl_utils"
sys.path.append(str(target_dir))

from cwl_utilities import call_cwltool  # noqa: E402
from cwl_utilities import create_input_yaml  # noqa: E402
from cwl_utilities import parse_cwl_arguments  # noqa: E402


def test_bash_xvg() -> None:
    """Test bash_xvg."""
    cwl_file = Path("bash_xvg.cwl")
    input_to_props = parse_cwl_arguments(cwl_file)

    input_xvg1_path = "rmsd1.xvg"
    input_xvg1_path = str(Path(__file__).resolve().parent / Path(input_xvg1_path))
    input_to_props["input_xvg1_path"]["path"] = input_xvg1_path

    input_xvg2_path = "rmsd2.xvg"
    input_xvg2_path = str(Path(__file__).resolve().parent / Path(input_xvg2_path))
    input_to_props["input_xvg2_path"]["path"] = input_xvg2_path

    input_to_props["output_xvg_path"] = "output.xvg"
    input_yaml_path = Path("bash_xvg.yml")
    create_input_yaml(input_to_props, input_yaml_path)
    call_cwltool(cwl_file, input_yaml_path)
    assert Path("output.xvg").exists()
