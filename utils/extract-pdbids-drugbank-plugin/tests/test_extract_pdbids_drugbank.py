"""Tests for extract_pdbids_drugbank."""
from pathlib import Path

from polus.mm.utils.extract_pdbids_drugbank.extract_pdbids_drugbank import (
    extract_pdbids_drugbank,
)


def test_extract_pdbids_drugbank() -> None:
    """Test extract_pdbids_drugbank."""
    # Fake SMILES
    inchi = ["InChI3491", "InChI8564", "InChI7556"]

    input_xml_path = "drugbank_10_fake_records_5.1.10.xml"
    input_xml_path = str(Path(__file__).resolve().parent / Path(input_xml_path))

    extract_pdbids_drugbank(input_xml_path, [], inchi, [], "out.txt")

    assert Path("out.txt").exists()
