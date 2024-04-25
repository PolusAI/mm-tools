"""CWL utilities."""
import subprocess
from pathlib import Path
from typing import Any

from ruamel.yaml import YAML


def modify_cwl_file(cwl_file: Path, format_dict: dict) -> str:
    """Modify the CWL file to include the format for the input file.

    If you have multiple file formats then cwltool will result in the error.
    ref_resolver.py", line 232, in expand_url
        if url.startswith("_:"):
    AttributeError: 'CommentedSeq' object has no attribute 'startswith'.

    Args:
        cwl_file (str): The path to the CWL file.
        format_dict (Dict): The dictionary of input names to their formats.
    """
    modified_cwl_file = f"{str(cwl_file).split('.')[0]}_modified.cwl"
    # replace format for given input with the provided format
    yaml = YAML(typ="safe", pure=True)
    with cwl_file.open(encoding="utf-8") as file:
        cwl_content = yaml.load(file)
        inputs = cwl_content.get("inputs", {})
        for input_name, input_data in inputs.items():
            if input_name in format_dict:
                input_data["format"] = format_dict[input_name]["format"]
                inputs[input_name] = input_data
        cwl_content["inputs"] = inputs
    with Path(modified_cwl_file).open("w", encoding="utf-8") as file:
        yaml.dump(cwl_content, file)
    return modified_cwl_file


def parse_cwl_arguments(cwl_file: Path) -> dict[str, Any]:
    """Parse the CWL file to get the required inputs.

    Args:
        cwl_file (Path): The path to the CWL file.

    Returns:
        Dict[str, Dict]: A dictionary of input names to their properties.
    """
    yaml = YAML(typ="safe", pure=True)
    with cwl_file.open(encoding="utf-8") as file:
        cwl_content = yaml.load(file)
    black_list_cwl_types = ["string?", "boolean?", "int?", "float?"]
    input_to_props: dict[str, Any] = {}
    inputs = cwl_content.get("inputs", {})
    for input_name, input_data in inputs.items():
        default_value = input_data.get("default", "")
        cwl_type = input_data.get("type", "")
        if isinstance(cwl_type, dict):
            the_type = cwl_type["type"]
            if the_type == "array":
                items = cwl_type["items"]
                cwl_type = f"{items}[]"
        # find inputs that are required
        if not default_value and cwl_type not in black_list_cwl_types:
            if cwl_type == "File" or cwl_type == "File?":
                cwl_format = input_data.get("format", "")
                file_dict = {"class": cwl_type, "path": "", "format": cwl_format}
                input_to_props[input_name] = file_dict
            elif cwl_type == "File[]":
                input_to_props[input_name] = []
                file_dict = {"class": "File", "path": "", "format": cwl_format}
                input_to_props[input_name].append(file_dict)
            elif cwl_type == "string[]" or cwl_type == "float[]" or cwl_type == "int[]":
                input_to_props[input_name] = []
            else:
                input_to_props[input_name] = cwl_type

    return input_to_props


def create_input_yaml(input_to_value: dict[str, str], output_yaml: Path) -> None:
    """Create the input YAML file.

    Args:
        input_to_value (Dict[str, str]): Dictionary of input names to their values.
        output_yaml (Path): Path to the output YAML file.
    """
    yaml = YAML()
    with output_yaml.open("w", encoding="utf-8") as file:
        yaml.dump(input_to_value, file)


def call_cwltool(cwl_file: Path, input_yaml_path: Path) -> None:
    """Call cwltool.

    Args:
        cwl_file (Path): The path to the CWL file.
        input_yaml_path (Path): The path to the input YAML file.
    """
    command = ["cwltool", "--debug", str(cwl_file), str(input_yaml_path)]
    completed_process = subprocess.run(
        command,
        capture_output=True,
        text=True,
    )
    return completed_process.stdout, completed_process.stderr
