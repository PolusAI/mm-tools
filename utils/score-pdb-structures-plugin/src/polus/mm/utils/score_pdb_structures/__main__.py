"""Package entrypoint for the score_pdb_structures package."""

# Base packages
import logging
from os import environ

import typer
from polus.mm.utils.score_pdb_structures.score_pdb_structures import (
    score_pdb_structures,
)

logging.basicConfig(
    format="%(asctime)s - %(name)-8s - %(levelname)-8s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
)
POLUS_LOG = getattr(logging, environ.get("POLUS_LOG", "INFO"))
logger = logging.getLogger("polus.mm.utils.score_pdb_structures.")
logger.setLevel(POLUS_LOG)

app = typer.Typer(help="score_pdb_structures.")


@app.command()
def main(  # noqa: PLR0913
    input_pdbids: list[str] = typer.Option(
        ...,
        "--input_pdbids",
        help="List of input PDBIDs to score, Type string[]",
    ),
    output_txt_path: str = typer.Option(
        ...,
        "--output_txt_path",
        help="Path to the text dataset file, Type string",
    ),
    min_row: int = typer.Option(
        ...,
        "--min_row",
        help="The row min inex, Type int",
    ),
    max_row: int = typer.Option(
        ...,
        "--max_row",
        help="The row max inex, Type int",
    ),
    timeout_duration: int = typer.Option(
        ...,
        "--timeout_duration",
        help="The maximum time to wait for a response from the API before timing out",
    ),
    max_retries: int = typer.Option(
        ...,
        "--max_retries",
        help="The maximum number of times to retry the request in case of failure",
    ),
) -> None:
    """score_pdb_structures."""
    logger.info(f"input_pdbids: {input_pdbids}")
    logger.info(f"output_txt_path: {output_txt_path}")
    logger.info(f"min_row: {min_row}")
    logger.info(f"max_row: {max_row}")
    logger.info(f"timeout_duration: {timeout_duration}")
    logger.info(f"max_retries: {max_retries}")

    score_pdb_structures(
        input_pdbids=input_pdbids,
        output_txt_path=output_txt_path,
        min_row=min_row,
        max_row=max_row,
        timeout_duration=timeout_duration,
        max_retries=max_retries,
    )


if __name__ == "__main__":
    app()
