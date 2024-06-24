"""Extract PDB IDs Drugbank XSData Plugin."""
from pathlib import Path
from typing import Optional

from drugbank_schemas.models.drugbank_latest import Drugbank
from rdkit import Chem
from xsdata.formats.dataclass.context import XmlContext
from xsdata_pydantic.bindings import XmlParser


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


def search_inchi(data: Drugbank, inchi_ids: list[str]) -> Drugbank:
    """Filters the Drugbank database uisng InChi.

    Args:
        data (Drugbank): The Drugbank data
        inchi_ids (list[str]): The input InChi of small molecules

    Returns:
         Drugbank: Filtered database
    """
    filtered_database = Drugbank()
    filtered_database.drug = []
    for drug in data.drug:
        if (
            drug.type_value.name == "SMALL_MOLECULE"
            and drug.calculated_properties is not None
        ):
            for prop in drug.calculated_properties.property:
                if prop.kind.name == "IN_CH_I" and prop.value in inchi_ids:
                    filtered_database.drug.append(drug)

    return filtered_database


def search_inchi_kyes(
    data: Drugbank,
    inchi_keys: list[str],
) -> Drugbank:
    """Filters the Drugbank database uisng InChi keys.

    Args:
        data (Drugbank): The Drugbank data
        inchi_keys (list[str]): The input InChi keys of small molecules

    Returns:
        Drugbank: Filtered database
    """
    filtered_database = Drugbank()
    filtered_database.drug = []
    for drug in data.drug:
        if (
            drug.type_value.name == "SMALL_MOLECULE"
            and drug.calculated_properties is not None
        ):
            for prop in drug.calculated_properties.property:
                if prop.kind.name == "IN_CH_IKEY" and prop.value in inchi_keys:
                    filtered_database.drug.append(drug)
    return filtered_database


def extract_pdbids_drugbank_xsdata(
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
    xml_file = Path(drugbank_xml_file_path)

    # Parse the XML file using the generated models
    parser = XmlParser(context=XmlContext())
    drug_data = parser.parse(xml_file, Drugbank)

    if smiles:
        inchi_ids = [
            smiles_to_inchi(sm) for sm in smiles
        ]  # smiles can be in different formats
        inchi_ids_clean = [inchi_id for inchi_id in inchi_ids if inchi_id is not None]
        search_inchi(drug_data, inchi_ids_clean)

    elif inchi:
        filtered_database = search_inchi(drug_data, inchi)

    elif inchi_keys:
        search_inchi_kyes(drug_data, inchi_keys)

    with Path.open(Path(output_txt_path), mode="w", encoding="utf-8") as f:
        for drug in filtered_database.drug:
            if drug.pdb_entries is not None and len(drug.pdb_entries.pdb_entry) > 0:
                pdb_ids = ",".join(drug.pdb_entries.pdb_entry)
                for prop in drug.calculated_properties.property:
                    if prop.kind.name == "SMILES":
                        smiles = prop.value
                        f.write(f"{smiles},{pdb_ids}\n")
