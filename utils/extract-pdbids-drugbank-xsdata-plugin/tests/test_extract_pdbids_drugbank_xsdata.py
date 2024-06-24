"""Tests for extract_pdbids_drugbank_xsdata."""
from pathlib import Path

from polus.mm.utils.extract_pdbids_drugbank_xsdata.extract_pdbids_drugbank_xsdata import (  # noqa: E501
    extract_pdbids_drugbank_xsdata,
)


def test_extract_pdbids_drugbank_xsdata() -> None:
    """Test extract_pdbids_drugbank_xsdata."""
    # Fake SMILES
    inchi = ["InChI3491", "InChI8564", "InChI7556"]

    input_xml_path = "drugbank_10_fake_records_5.1.10.xml"

    input_xml_path = str(Path(__file__).resolve().parent / Path(input_xml_path))

    extract_pdbids_drugbank_xsdata(input_xml_path, [], inchi, [], "out.txt")

    assert Path("out.txt").exists()
