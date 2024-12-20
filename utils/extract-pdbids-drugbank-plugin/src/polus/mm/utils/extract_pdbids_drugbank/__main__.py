"""Package entrypoint for the extract_pdbids_drugbank package."""
import argparse
import logging
from os import environ

from polus.mm.utils.extract_pdbids_drugbank.extract_pdbids_drugbank import (
    extract_pdbids_drugbank,
)

logging.basicConfig(
    format="%(asctime)s - %(name)-8s - %(levelname)-8s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
)
POLUS_LOG = getattr(logging, environ.get("POLUS_LOG", "INFO"))
logger = logging.getLogger("polus.mm.utils.extract_pdbids_drugbank.")
logger.setLevel(POLUS_LOG)


def main() -> None:
    """extract_pdbids_drugbank."""
    parser = argparse.ArgumentParser(
        description="Extract PDB IDs from Drugbank XML using various"
        "chemical identifiers.",
    )

    # Define arguments
    parser.add_argument(
        "--drugbank_xml_file_path",
        type=str,
        required=True,
        help="Path to the Drugbank XML file",
    )
    parser.add_argument(
        "--smiles",
        type=str,
        nargs="+",
        required=False,
        help="List of input SMILES, Type string[], File type input,"
        "Accepted formats: list[string]",
    )
    parser.add_argument(
        "--inchi",
        type=str,
        nargs="+",
        required=False,
        help="List of input InChIs, Type string[], File type input",
    )
    parser.add_argument(
        "--inchi_keys",
        type=str,
        nargs="+",
        required=False,
        help="List of input InChI Keys, Type string[], File type input",
    )
    parser.add_argument(
        "--output_txt_path",
        type=str,
        required=True,
        help="Path to the text dataset file, Type string, File type output",
    )

    # Parse the arguments
    args = parser.parse_args()

    # Log the arguments
    logger.info(f"drugbank_xml_file_path: {args.drugbank_xml_file_path}")
    logger.info(f"smiles: {args.smiles}")
    logger.info(f"inchi: {args.inchi}")
    logger.info(f"inchi_keys: {args.inchi_keys}")
    logger.info(f"output_txt_path: {args.output_txt_path}")

    # Call the main function from the module
    extract_pdbids_drugbank(
        drugbank_xml_file_path=args.drugbank_xml_file_path,
        smiles=args.smiles,
        inchi=args.inchi,
        inchi_keys=args.inchi_keys,
        output_txt_path=args.output_txt_path,
    )


if __name__ == "__main__":
    main()
