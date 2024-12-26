"""Package entrypoint for the score_pdb_structures package."""

# Base packages
import argparse
import logging
from os import environ

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


def main(args: argparse.Namespace) -> None:
    """score_pdb_structures."""
    logger.info(f"input_pdbids: {args.input_pdbids}")
    logger.info(f"output_txt_path: {args.output_txt_path}")
    logger.info(f"min_row: {args.min_row}")
    logger.info(f"max_row: {args.max_row}")
    logger.info(f"timeout_duration: {args.timeout_duration}")
    logger.info(f"max_retries: {args.max_retries}")

    score_pdb_structures(
        input_pdbids=args.input_pdbids,
        output_txt_path=args.output_txt_path,
        min_row=args.min_row,
        max_row=args.max_row,
        timeout_duration=args.timeout_duration,
        max_retries=args.max_retries,
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="score_pdb_structures.")
    parser.add_argument(
        "--input_pdbids",
        type=str,
        nargs="+",
        required=True,
        help="List of input PDBIDs to score, Type string[]",
    )
    parser.add_argument(
        "--output_txt_path",
        type=str,
        required=True,
        help="Path to the text dataset file, Type string",
    )
    parser.add_argument(
        "--min_row",
        type=int,
        required=True,
        help="The row min index, Type int",
    )
    parser.add_argument(
        "--max_row",
        type=int,
        required=True,
        help="The row max index, Type int",
    )
    parser.add_argument(
        "--timeout_duration",
        type=int,
        required=True,
        help="The maximum time to wait for a response from the API before timing out",
    )
    parser.add_argument(
        "--max_retries",
        type=int,
        required=True,
        help="The maximum number of times to retry the request in case of failure",
    )

    args = parser.parse_args()
    main(args)
