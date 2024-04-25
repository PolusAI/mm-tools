"""Tests for {{cookiecutter.package_name}}."""
import sys
from pathlib import Path

current_dir = Path(__file__).resolve().parent
target_dir = current_dir.parent.parent.parent / 'cwl_utils'
sys.path.append(str(target_dir))

from cwl_utilities import call_cwltool  # noqa: E402
from cwl_utilities import create_input_yaml  # noqa: E402
from cwl_utilities import parse_cwl_arguments  # noqa: E402

from {{cookiecutter.plugin_package}}.{{cookiecutter.package_name}} import (
    {{cookiecutter.package_name}},
)