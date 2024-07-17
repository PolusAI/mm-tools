"""Tests for score_pdb_structures."""
from pathlib import Path

from polus.mm.utils.score_pdb_structures.score_pdb_structures import (
    score_pdb_structures,
)


def test_score_pdb_structures() -> None:
    """Test score_pdb_structures."""
    input_pdbids = [
        "1aod",
        "1g0i",
        "1iev",
        "1ptg",
        "1y7v",
        "2huo",
        "2os9",
        "2r71",
        "2x1i",
        "3bxd",
    ]
    score_pdb_structures(input_pdbids, "output.txt", max_row=1)

    assert Path("output.txt").exists()
