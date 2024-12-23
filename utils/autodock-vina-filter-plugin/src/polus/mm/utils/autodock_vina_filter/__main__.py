"""Package entrypoint for the autodock_vina_filter package."""

# Base packages
import logging
from os import environ
from pathlib import Path
from typing import List

import typer
from polus.mm.utils.autodock_vina_filter.autodock_vina_filter import (
    autodock_vina_filter,
)

logging.basicConfig(
    format="%(asctime)s - %(name)-8s - %(levelname)-8s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
)
POLUS_LOG = getattr(logging, environ.get("POLUS_LOG", "INFO"))
logger = logging.getLogger("polus.mm.utils.autodock_vina_filter.")
logger.setLevel(POLUS_LOG)

app = typer.Typer(help="autodock_vina_filter.")



@app.command()
def main(
    input_log_path: str = typer.Option(
        ...,
        '--input_log_path',
        help='Path to the log file, Type: string, File type: output, Accepted formats: log, Example file: https://github.com/bioexcel/biobb_vs/raw/master/biobb_vs/test/reference/vina/ref_output_vina.log',
    ),
    input_log_paths: List[str] = typer.Option(
        ...,
        '--input_log_paths',
        help='Path to the log files, Type: string, File type: output, Accepted formats: log, Example file: https://github.com/bioexcel/biobb_vs/raw/master/biobb_vs/test/reference/vina/ref_output_vina.log',
    ),
    docking_score_cutoff: float = typer.Option(
        ...,
        '--docking_score_cutoff',
        help='Cutoff threshold for filtering docking scores, Type: float',
    ),
    max_num_poses_per_ligand: int = typer.Option(
        ...,
        '--max_num_poses_per_ligand',
        help='Maximum number of poses per initial ligand, Type: int',
    ),
    max_num_poses_total: int = typer.Option(
        ...,
        '--max_num_poses_total',
        help='Maximum number of poses total, Type: int',
    ),
    input_txt_path: str = typer.Option(
        ...,
        '--input_txt_path',
        help='Experimental binding free energy data file (if any)',
    ),
    rescore: bool = typer.Option(
        ...,
        '--rescore',
        help='Use True if autodock vina was run with --rescore',
    ),

) -> None:
    """autodock_vina_filter."""
    logger.info(f"input_log_path: {input_log_path}")
    logger.info(f"input_log_paths: {input_log_paths}")
    logger.info(f"docking_score_cutoff: {docking_score_cutoff}")
    logger.info(f"max_num_poses_per_ligand: {max_num_poses_per_ligand}")
    logger.info(f"max_num_poses_total: {max_num_poses_total}")
    logger.info(f"input_txt_path: {input_txt_path}")
    logger.info(f"rescore: {rescore}")

    autodock_vina_filter(
    input_log_path=input_log_path,
    input_log_paths=input_log_paths,
    docking_score_cutoff=docking_score_cutoff,
    max_num_poses_per_ligand=max_num_poses_per_ligand,
    max_num_poses_total=max_num_poses_total,
    input_txt_path=input_txt_path,
    rescore=rescore)
    
    
if __name__ == '__main__':
    app()