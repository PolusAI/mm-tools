"""Modify the base template to add input and output options dynamically."""
import contextlib
import json
import shutil
from pathlib import Path

# Load cookiecutter.json
json_path = Path("cookiecutter.json")

with json_path.open() as json_file:
    cookiecutter_data = json.load(json_file)


def add_readme_options_dynamically(cookiecutter_json: dict) -> None:
    """Add the Options section to the README.md file dynamically.

    Args:
        cookiecutter_json (Dict): The cookiecutter.json file as a dictionary.
    """
    # Create the Options section dynamically
    options_section = "## Options\n\nThis plugin takes {} input arguments\
    and {} output argument:\n\n".format(
        len(cookiecutter_json["inputs"]),
        len(cookiecutter_json["outputs"]),
    )

    # Add the table headers
    options_section += (
        "| Name          | Description             | I/O    | Type   | Default |\n"
    )
    options_section += (
        "|---------------|-------------------------|--------|--------|---------|\n"
    )

    # Add rows for input arguments
    for input_name, input_data in cookiecutter_json["inputs"].items():
        options_section += "| {} | {} | {} | {} | {} |\n".format(
            input_name,
            input_data["description"],
            "Input",
            input_data["type"],
            input_data["type"],
        )

    # Add rows for output arguments
    for output_name, output_data in cookiecutter_json["outputs"].items():
        options_section += "| {} | {} | {} | {} | {} |\n".format(
            output_name,
            output_data["description"],
            "Output",
            output_data["type"],
            output_data["type"],
        )
    path = Path("{{cookiecutter.container_name}}") / "README.md"

    with path.open("a") as updated_readme_file:
        updated_readme_file.write(options_section)


def add_function_arguments_dynamically(cookiecutter_json: dict) -> None:
    """Add the function arguments to the plugin file.

    Args:
        cookiecutter_json (Dict): The cookiecutter.json file as a dictionary.
    """
    package_name = cookiecutter_json["plugin_package"].split(".")[-1]
    def_string = f"def {package_name}("
    dict_items = ["inputs", "outputs"]
    # add top level imports
    import_string = "from typing import List\nfrom pathlib import Path\n"
    # create definition string
    for item in dict_items:
        for key, value in cookiecutter_json[item].items():
            # use filepattern in __main__ to pass multiple files form inpdir
            if key == "inpdir":
                continue
            if "python_type" in value:
                def_string += f"{key} : {value['python_type']}, "
            elif "_pattern" in key:
                original_key = key.replace("_pattern", "")
                new_python_type = "List[Path]"
                def_string += f"{original_key}: {new_python_type}, "
    def_string = def_string[:-2] + "):"
    # now add the docstring
    docstring = f"    '''{cookiecutter_json['plugin_name']}.\n\n    Args:\n"
    for item in dict_items:
        for key, value in cookiecutter_json[item].items():
            if key == "inpdir":
                continue
            if "python_type" in value:
                docstring += f"        {key}: {value['description']}\n"
            elif "_pattern" in key:
                original_key = key.replace("_pattern", "")
                docstring += f"        {original_key}: {value['description']}\n"
    path = (
        Path("{{cookiecutter.container_name}}")
        / "src"
        / "{{cookiecutter.package_folders}}"
        / "{{cookiecutter.package_name}}.py"
    )

    with path.open("a") as file:
        file.write(
            import_string
            + "\n"
            + def_string
            + "\n"
            + docstring
            + "    Returns:\n        None\n    '''\n    pass\n",
        )


def add_main_function_dynamically(cookiecutter_json: dict) -> None:
    """Add the main function to the __main__.py file.

    Args:
        cookiecutter_json (Dict): The cookiecutter.json file as a dictionary.
    """
    # Create the main function string
    main_function_string = "\n\n@app.command()\ndef main("

    dict_items = ["inputs", "outputs"]
    for item in dict_items:
        for key, value in cookiecutter_json[item].items():
            main_function_string += (
                f"\n    {key}: {value['python_type']} = typer.Option("
            )
            main_function_string += "\n        ...,"
            main_function_string += f"\n        '--{key}',"
            main_function_string += f"\n        help='{value['description']}',"
            main_function_string += "\n    ),"

    # Add the main function body
    main_function_string += "\n) -> None:"
    main_function_string += f'\n    """{cookiecutter_json["plugin_name"]}."""'
    for item in dict_items:
        for key in cookiecutter_json[item]:
            main_function_string += f'\n    logger.info(f"{key}: {{{key}}}")'

    package_name = cookiecutter_json["plugin_package"].split(".")[-1]
    main_function_string += f"\n\n    {package_name}("
    for item in dict_items:
        for key in cookiecutter_json[item]:
            main_function_string += f"\n    {key}={key},"
    main_function_string = main_function_string[:-1] + ")"
    main_function_string += "\n\nif __name__ == '__main__':"
    main_function_string += "\n    app()"

    # Check if the __main__.py file exists
    main_file_path = (
        Path("{{cookiecutter.container_name}}")
        / "src"
        / "{{cookiecutter.package_folders}}"
        / "__main__.py"
    )

    with main_file_path.open("a") as file:
        file.write(main_function_string)


def add_ict_inputs_outputs_dynamically(cookiecutter_json: dict) -> None:
    """Add the input and output options to the ict.yml file.

    Args:
        cookiecutter_json (Dict): The cookiecutter.json file as a dictionary.
    """
    path = Path("{{cookiecutter.container_name}}") / "ict.yml"

    array = ["inputs", "outputs"]
    with path.open("a") as updated_ict_file:
        for item in array:
            updated_ict_file.write(f"{item}:\n")
            for key, value in cookiecutter_json[item].items():
                updated_ict_file.write(f"  - name: {key}\n")
                updated_ict_file.write("    required: true\n")
                updated_ict_file.write(f"    description: {value['description']}\n")
                updated_ict_file.write(f"    type: {value['type']}\n")
                if "default" in value:
                    updated_ict_file.write(f"    defaultValue: {value['default']}\n")
                if "format" in value:
                    uris = value["format"]
                    uris = ", ".join(uris)
                    updated_ict_file.write("    format:\n")
                    updated_ict_file.write(f"      uri: {uris}\n")
        updated_ict_file.write("ui:\n")
        for key, value in cookiecutter_json["inputs"].items():
            updated_ict_file.write(f"  - key: inputs.{key}\n")
            updated_ict_file.write(f'    title: "{key}: "\n')
            updated_ict_file.write(f"    description: \"{value['description']}\"\n")
            # type can be text, number, checkbox, path or file
            # if incoming type is boolean, then type is checkbox
            if value["type"] == "boolean":
                value["type"] = "checkbox"
            updated_ict_file.write(f"    type: {value['type']}\n")


# need to handle cases where base_command is just python3
# calling some script already in container for example
ADD_SOURCE = False
base_command = cookiecutter_data["base_command"]
if "arguments" in cookiecutter_data:
    arguments = cookiecutter_data["arguments"]
    # combine base_command and arguments need to determine if source is needed
    base_command = base_command + " " + arguments
# look for .py file in base_command
for item in base_command.split():
    if ".py" in item or "python" in item:
        ADD_SOURCE = True
        break

add_readme_options_dynamically(cookiecutter_data)
add_ict_inputs_outputs_dynamically(cookiecutter_data)
if ADD_SOURCE:
    add_function_arguments_dynamically(cookiecutter_data)
    add_main_function_dynamically(cookiecutter_data)
    cookiecutter_data[
        "base_command"
    ] = f"python3 -m {cookiecutter_data['plugin_package']}"
    with json_path.open("w") as json_file:
        json.dump(cookiecutter_data, json_file, indent=4)
else:
    src_folder = Path("{{cookiecutter.container_name}}") / "src"
    with contextlib.suppress(FileNotFoundError):
        shutil.rmtree(src_folder)

    dockerfile = Path("{{cookiecutter.container_name}}") / "Dockerfile"
    build_docker = Path("{{cookiecutter.container_name}}") / "build-docker.sh"
    dockerfile.unlink()
    build_docker.unlink()

    pyproject = Path("{{cookiecutter.container_name}}") / "pyproject.toml"
    with pyproject.open("r") as read_file:
        lines = read_file.readlines()

    with pyproject.open("w") as write_file:
        for line in lines:
            if "packages = [" not in line:
                write_file.write(line)
