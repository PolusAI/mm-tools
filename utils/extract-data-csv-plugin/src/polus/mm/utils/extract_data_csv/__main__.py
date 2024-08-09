"""Package entrypoint for the extract_data_csv package."""

# Base packages
import logging
from os import environ

import typer
from polus.mm.utils.extract_data_csv.extract_data_csv import extract_data_csv

logging.basicConfig(
    format="%(asctime)s - %(name)-8s - %(levelname)-8s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
)
POLUS_LOG = getattr(logging, environ.get("POLUS_LOG", "INFO"))
logger = logging.getLogger("polus.mm.utils.extract_data_csv.")
logger.setLevel(POLUS_LOG)

app = typer.Typer(help="extract_data_csv.")


@app.command()
def main(  # noqa: PLR0913
    input_csv_path: str = typer.Option(
        ...,
        "--input_csv_path",
        help="Path to the input csv file, Type string, File type input",
    ),
    query: str = typer.Option(
        ...,
        "--query",
        help="query str to search the dataset, Type string, File type input",
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
    column_name: str = typer.Option(
        ...,
        "--column_name",
        help="The name of the column to load data, Type string, File type input",
    ),
    output_txt_path: str = typer.Option(
        ...,
        "--output_txt_path",
        help="Path to the txt datoutput file, Type string, File type output",
    ),
) -> None:
    """extract_data_csv."""
    logger.info(f"input_csv_path: {input_csv_path}")
    logger.info(f"query: {query}")
    logger.info(f"min_row: {min_row}")
    logger.info(f"max_row: {max_row}")
    logger.info(f"column_name: {column_name}")
    logger.info(f"output_txt_path: {output_txt_path}")

    extract_data_csv(
        input_csv_path=input_csv_path,
        query=query,
        min_row=min_row,
        max_row=max_row,
        column_name=column_name,
        output_txt_path=output_txt_path,
    )


if __name__ == "__main__":
    app()
