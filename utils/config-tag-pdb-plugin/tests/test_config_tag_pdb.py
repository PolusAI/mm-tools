"""Tests for config_tag_pdb."""
import sys
from pathlib import Path

current_dir = Path(__file__).resolve().parent
target_dir = current_dir.parent.parent.parent / "cwl_utils"
sys.path.append(str(target_dir))

from cwl_utilities import call_cwltool  # noqa: E402
from cwl_utilities import create_input_yaml  # noqa: E402
from cwl_utilities import parse_cwl_arguments  # noqa: E402


def test_config_tag_pdb() -> None:
    """Test config_tag_pdb."""
    cwl_file = Path("config_tag_pdb.cwl")
    input_to_props = parse_cwl_arguments(cwl_file)

    input_to_props["pdb_id"] = "4xk9"
    input_to_props["filter"] = "False"

    input_yaml_path = Path("config_tag_pdb.yml")

    create_input_yaml(input_to_props, input_yaml_path)
    stdout, stderr = call_cwltool(cwl_file, input_yaml_path)
    assert "success" in stderr
