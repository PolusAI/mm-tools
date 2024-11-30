"""Package entrypoint for the extract_pdbids_drugbank_xsdata package."""

# Base packages
import argparse
import logging
from os import environ

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


def main(args: argparse.Namespace) -> None:
    """extract_pdbids_drugbank_xsdata."""
    logger.info(f"drugbank_xml_file_path: {args.drugbank_xml_file_path}")
    logger.info(f"smiles: {args.smiles}")
    logger.info(f"inchi: {args.inchi}")
    logger.info(f"inchi_keys: {args.inchi_keys}")
    logger.info(f"output_txt_path: {args.output_txt_path}")

    extract_pdbids_drugbank_xsdata(
        drugbank_xml_file_path=args.drugbank_xml_file_path,
        smiles=args.smiles,
        inchi=args.inchi,
        inchi_keys=args.inchi_keys,
        output_txt_path=args.output_txt_path,
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="extract_pdbids_drugbank_xsdata.")

    parser.add_argument(
        "--drugbank_xml_file_path",
        type=str,
        required=True,
        help="Path to the Drugbank xml file",
    )
    parser.add_argument(
        "--smiles",
        type=str,
        nargs="+",
        required=True,
        help="List of input SMILES, Type string[], File type input",
    )
    parser.add_argument(
        "--inchi",
        type=str,
        nargs="+",
        required=True,
        help="List of input InChI, Type string[], File type input",
    )
    parser.add_argument(
        "--inchi_keys",
        type=str,
        nargs="+",
        required=True,
        help="List of input InChI keys, Type string[], File type input",
    )
    parser.add_argument(
        "--output_txt_path",
        type=str,
        required=True,
        help="Path to the text dataset file, Type string, File type output",
    )

    args = parser.parse_args()
    main(args)
