"""Extract PDB IDs Drugbank Plugin."""
import collections
from pathlib import Path
from typing import Optional

import pandas as pd
from defusedxml.ElementTree import parse
from rdkit import Chem


# The code is adapted from https://github.com/dhimmel/drugbank/blob/gh-pages/parse.ipynb
def parse_drugbank_xml(drugbank_xml_path: str) -> pd.DataFrame:
    """Parse the DrugBank XML file into a data frame.

    Args:
        drugbank_xml_path (str): The path to the drugbank xml file

    Returns:
        pd.DataFrame: The proccesd Drugbank
    """
    ns = "{http://www.drugbank.ca}"
    inchikey_template = (
        f"{ns}calculated-properties/{ns}property[{ns}kind='InChIKey']/{ns}value"
    )
    inchi_template = (
        f"{ns}calculated-properties/{ns}property[{ns}kind='InChI']/{ns}value"
    )
    smiles_template = (
        f"{ns}calculated-properties/{ns}property[{ns}kind='SMILES']/{ns}value"
    )

    xtree = parse(drugbank_xml_path)
    root = xtree.getroot()
    rows = []
    for drug in root:
        row = collections.OrderedDict()

        row["name"] = drug.findtext(f"{ns}name")
        row["type"] = drug.get("type")
        row["drugbank_id"] = drug.findtext(ns + "drugbank-id[@primary='true']")
        row["groups"] = [group.text for group in drug.findall(f"{ns}groups/{ns}group")]
        row["inchi"] = drug.findtext(inchi_template)
        row["inchikey"] = drug.findtext(inchikey_template)
        row["smiles"] = drug.findtext(smiles_template)

        pdb_ids = drug.find(f"{ns}pdb-entries")
        if pdb_ids is not None:
            target_ids = []
            for pdb_id in pdb_ids:
                target_ids.append(str(pdb_id.text))

            row["pdb_entries"] = ",".join(target_ids)

        rows.append(row)

    columns = [
        "drugbank_id",
        "name",
        "type",
        "groups",
        "inchi",
        "inchikey",
        "smiles",
        "pdb_entries",
    ]
    drugbank_df = pd.DataFrame.from_dict(rows)[columns]

    return drugbank_df[
        drugbank_df.smiles.map(lambda x: x is not None)
        & drugbank_df.type.map(lambda x: x == "small molecule")
    ]


def smiles_to_inchi(smiles: str) -> Optional[str]:
    """Converts SMILES to InChI.

    Args:
        smiles (str): The SMILES of small molecules

    Returns:
        str: The InChi key
    """
    # Convert SMILES to RDKit molecule object
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        print(f"Error: Invalid SMILES string: {smiles}")  # noqa: T201
        return None

    # Convert molecule to InChI
    return Chem.MolToInchi(mol)


def extract_pdbids_drugbank(
    drugbank_xml_file_path: str,
    smiles: list[str],
    inchi: list[str],
    inchi_keys: list[str],
    output_txt_path: str,
) -> None:
    """Filter DrugBank based on a list of small molecules.

    Args:
        drugbank_xml_file_path: Path to the Drugbank xml file
        smiles: List of input SMILES, Type string[], File type input
        inchi: List of input SMILES, Type string[], File type input
        inchi_keys: List of input SMILES, Type string[], File type input
        output_txt_path: Path to the text dataset file, Type string, File type output
    Returns:
        None.
    """
    drugbank = parse_drugbank_xml(drugbank_xml_file_path)

    if smiles:
        inchi_ids = [
            smiles_to_inchi(sm) for sm in smiles
        ]  # smiles can be in different formats
        inchi_ids = [inchi_id for inchi_id in inchi_ids if inchi_id is not None]
        filtered_df = drugbank[drugbank["inchi"].isin(inchi_ids)]

    elif inchi:
        filtered_df = drugbank[drugbank["inchi"].isin(inchi)]

    elif inchi_keys:
        filtered_df = drugbank[drugbank["inchikey"].isin(inchi_keys)]

    with Path.open(Path(output_txt_path), mode="w", encoding="utf-8") as f:
        for _, row in filtered_df.iterrows():
            if row["pdb_entries"]:
                f.write(f"{row['smiles']},{row['pdb_entries']}\n")