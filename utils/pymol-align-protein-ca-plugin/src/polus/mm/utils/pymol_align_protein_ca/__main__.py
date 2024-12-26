"""Package entrypoint for the pymol_align_protein_ca package."""

# Base packages
import logging
from os import environ

import typer
from polus.mm.utils.pymol_align_protein_ca.pymol_align_protein_ca import (
    pymol_align_protein_ca,
)

logging.basicConfig(
    format="%(asctime)s - %(name)-8s - %(levelname)-8s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
)
POLUS_LOG = getattr(logging, environ.get("POLUS_LOG", "INFO"))
logger = logging.getLogger("polus.mm.utils.pymol_align_protein_ca.")
logger.setLevel(POLUS_LOG)

app = typer.Typer(help="pymol_align_protein_ca.")


@app.command()
def main(
    input_1_path: str = typer.Option(
        ...,
        "--input_1_path",
        help="Input receptor file path",
    ),
    input_2_path: str = typer.Option(
        ...,
        "--input_2_path",
        help="Input ligand file path",
    ),
    input_3_path: str = typer.Option(
        ...,
        "--input_3_path",
        help="Input structure file path",
    ),
    input_4_path: str = typer.Option(
        ...,
        "--input_4_path",
        help="Input trajectory file path",
    ),
    output_file_path: str = typer.Option(
        ...,
        "--output_file_path",
        help="Path to the output file",
    ),
) -> None:
    """pymol_align_protein_ca."""
    logger.info(f"input_1_path: {input_1_path}")
    logger.info(f"input_2_path: {input_2_path}")
    logger.info(f"input_3_path: {input_3_path}")
    logger.info(f"input_4_path: {input_4_path}")
    logger.info(f"output_file_path: {output_file_path}")

    pymol_align_protein_ca(
        input_1_path=input_1_path,
        input_2_path=input_2_path,
        input_3_path=input_3_path,
        input_4_path=input_4_path,
        output_file_path=output_file_path,
    )


if __name__ == "__main__":
    app()
