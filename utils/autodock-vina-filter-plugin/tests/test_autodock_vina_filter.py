"""Tests for autodock_vina_filter."""
import sys
from pathlib import Path

from polus.mm.utils.autodock_vina_filter.autodock_vina_filter import (
    autodock_vina_filter,
)

current_dir = Path(__file__).resolve().parent
target_dir = current_dir.parent.parent.parent / "cwl_utils"
sys.path.append(str(target_dir))

from cwl_utilities import call_cwltool  # noqa: E402
from cwl_utilities import create_input_yaml  # noqa: E402
from cwl_utilities import parse_cwl_arguments  # noqa: E402


def test_autodock_vina_filter() -> None:
    """Test autodock_vina_filter."""
    input_log_paths = None
    input_log_path = "vina.log"
    input_txt_path = "binding_data.txt"
    docking_score_cutoff = -1.0
    max_num_poses_per_ligand = 1
    max_num_poses_total = 1
    rescore = True
    input_log_path = str(Path(__file__).resolve().parent / Path(input_log_path))
    input_txt_path = str(Path(__file__).resolve().parent / Path(input_txt_path))

    autodock_vina_filter(
        input_log_path,
        input_log_paths,
        docking_score_cutoff,
        max_num_poses_per_ligand,
        max_num_poses_total,
        input_txt_path,
        rescore,
    )
    assert Path("indices.txt").exists()


def test_cwl_autodock_vina_filter() -> None:
    """Test autodock_vina_filter in cwltool."""
    cwl_file = Path("autodock_vina_filter.cwl")
    input_to_props = parse_cwl_arguments(cwl_file)

    input_log_path = "vina.log"
    input_log_path = str(Path(__file__).resolve().parent / Path(input_log_path))
    input_to_props["input_log_path"]["path"] = [input_log_path]
    input_to_props["input_log_path"]["class"] = "File"

    input_txt_path = "binding_data.txt"
    input_txt_path = str(Path(__file__).resolve().parent / Path(input_txt_path))
    input_to_props["input_txt_path"]["path"] = input_txt_path
    input_to_props["input_txt_path"]["class"] = "File"

    input_ligand_pdbqt_path = "1e3g.pdqt"
    input_ligand_pdbqt_path = str(
        Path(__file__).resolve().parent / Path(input_ligand_pdbqt_path),
    )
    input_to_props["input_ligand_pdbqt_path"] = f"['{input_ligand_pdbqt_path}']"

    input_receptor_pdbqt_path = "1e3g_protein.pdb"
    input_receptor_pdbqt_path = str(
        Path(__file__).resolve().parent / Path(input_receptor_pdbqt_path),
    )
    input_to_props["input_receptor_pdbqt_path"] = f"['{input_receptor_pdbqt_path}']"

    input_to_props["docking_score_cutoff"] = -1.0
    input_to_props["max_num_poses_per_ligand"] = 1
    input_to_props["max_num_poses_total"] = 1
    input_to_props["rescore"] = True

    del input_to_props["input_log_paths"]
    input_yaml_path = Path("autodock_vina_filter.yml")
    create_input_yaml(input_to_props, input_yaml_path)
    call_cwltool(cwl_file, input_yaml_path)

    assert Path("indices.txt").exists()
