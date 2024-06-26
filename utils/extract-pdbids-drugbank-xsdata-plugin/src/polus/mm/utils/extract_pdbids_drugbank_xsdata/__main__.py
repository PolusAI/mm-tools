"""Package entrypoint for the extract_pdbids_drugbank_xsdata package."""

# Base packages
import logging
from os import environ

import typer
from polus.mm.utils.extract_pdbids_drugbank_xsdata.extract_pdbids_drugbank_xsdata import (  # noqa: E501
    extract_pdbids_drugbank_xsdata,
)

logging.basicConfig(
    format="%(asctime)s - %(name)-8s - %(levelname)-8s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
)
POLUS_LOG = getattr(logging, environ.get("POLUS_LOG", "INFO"))
logger = logging.getLogger("polus.mm.utils.extract_pdbids_drugbank_xsdata.")
logger.setLevel(POLUS_LOG)

app = typer.Typer(help="extract_pdbids_drugbank_xsdata.")


@app.command()
def main(
    drugbank_xml_file_path: str = typer.Option(
        ...,
        "--drugbank_xml_file_path",
        help="Path to the Drugbank xml file",
    ),
    smiles: list[str] = typer.Option(
        ...,
        "--smiles",
        help="List of input SMILES, Type string[], File type input",
    ),
    inchi: list[str] = typer.Option(
        ...,
        "--inchi",
        help="List of input SMILES, Type string[], File type input",
    ),
    inchi_keys: list[str] = typer.Option(
        ...,
        "--inchi_keys",
        help="List of input SMILES, Type string[], File type input",
    ),
    output_txt_path: str = typer.Option(
        ...,
        "--output_txt_path",
        help="Path to the text dataset file, Type string, File type output",
    ),
) -> None:
    """extract_pdbids_drugbank_xsdata."""
    logger.info(f"drugbank_xml_file_path: {drugbank_xml_file_path}")
    logger.info(f"smiles: {smiles}")
    logger.info(f"inchi: {inchi}")
    logger.info(f"inchi_keys: {inchi_keys}")
    logger.info(f"output_txt_path: {output_txt_path}")

    extract_pdbids_drugbank_xsdata(
        drugbank_xml_file_path=drugbank_xml_file_path,
        smiles=smiles,
        inchi=inchi,
        inchi_keys=inchi_keys,
        output_txt_path=output_txt_path,
    )


if __name__ == "__main__":
    app()
