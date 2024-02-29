# Initial Setup
```
sudo apt update
sudo apt install pipx
pipx ensurepath
pipx install poetry
pipx install bump2version
pipx install cookiecutter
pipx install ruamel.yaml
pipx install pre-commit # for code sanitation
cd ~/mm-tools
pre-commit install
```

# Create New Tool
```
cp ~/mm-workflows/cwl_adapters/extract_pdbbind_refined.cwl .
python read_cwl_inputs_outputs.py extract_pdbbind_refined.cwl
```

# Modify cookiecutter.json as needed
```
python modify_base_template.py
pipx run cookiecutter . --no-input
cd new_tool_created
```
# Modify pyproject.toml
# Modify Dockerfile
# Modify python source file, remove argparse, copy source code etc…
# Build container

# Add tests
```
pipx run poetry install
pipx run poetry run pytest
```

# Post Development
```
mv new_tool_created ../.
pipx run bump2version dev --dry-run —verbose
```
