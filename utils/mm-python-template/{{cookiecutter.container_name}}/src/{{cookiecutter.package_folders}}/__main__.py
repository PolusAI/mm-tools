"""Package entrypoint for the {{cookiecutter.package_name}} package."""

# Base packages
import logging
from os import environ
from pathlib import Path

import typer
from {{cookiecutter.plugin_package}}.{{cookiecutter.package_name}} import (
    {{cookiecutter.package_name}},
)

logging.basicConfig(
    format="%(asctime)s - %(name)-8s - %(levelname)-8s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
)
POLUS_LOG = getattr(logging, environ.get("POLUS_LOG", "INFO"))
logger = logging.getLogger("{{cookiecutter.plugin_package}}.")
logger.setLevel(POLUS_LOG)

app = typer.Typer(help="{{cookiecutter.plugin_name}}.")

