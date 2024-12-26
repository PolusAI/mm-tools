"""Align Protein and CA atoms for a trajectory using Pymol."""
import subprocess as sub

import pymol


def pymol_align_protein_ca(
    input_1_path: str,
    input_2_path: str,
    input_3_path: str,
    input_4_path: str,
    output_file_path: str,
) -> None:
    """pymol_align_protein_ca.

    Args:
        script:
        input_1_path: Input receptor file path
        input_2_path: Input ligand file path
        input_3_path: Input structure file path
        input_4_path: Input trajectory file path
        output_file_path: Path to the output file
    Returns:
        None
    """
    pymol.cmd.load(input_1_path, "receptor")
    pymol.cmd.load(input_2_path, "ligand")

    receptor = pymol.cmd.select("R", "receptor")
    # This assumes the receptor atoms are first in the file.
    indices_receptor = " or ".join([f"index {i}" for i in range(1, 1 + int(receptor))])

    ligand = pymol.cmd.select("L", "ligand")
    # This assumes the ligand atoms are appended to the file after the receptor.
    indices_ligand = " or ".join(
        [
            f"index {i}"
            for i in range(1 + int(receptor), 1 + int(receptor) + int(ligand))
        ],
    )

    pymol.cmd.load(input_3_path, "genion")
    pymol.cmd.select("G", f"genion and name CA and ({indices_receptor})")

    # NOTE: We do NOT want to load prod.gro here because the coordinates only get
    # written after the last timestep, so we can't use it for realtime analysis.
    # However, pymol just needs to extract the topology information, so we can use
    # genion.gro and overwrite the coordinates from the trajectory file prod.trr
    pymol.cmd.load(input_3_path, "prod")
    interval = 1  # Only load every nth frame.

    # NOTE: Pymol performs an alignment using an average across all
    # frames in the trajectory;
    # See https://sourceforge.net/p/pymol/mailman/message/29514454/
    # It does NOT perform a separate alignment for each frame!
    # (That's what we really want because e.g. gromacs cannot remove
    # the angular drift when using a periodic simulation box. It can
    # still remove the linear drift, however. This is probably fine
    # for very short simulations, but eventually the angular drift may
    # drift may inflate the rmsd of the ligand w.r.t. the docked conformation.
    # This is bad because we really want to avoid false negatives.)

    align_separately = False
    if align_separately:
        # We can process each frame individually and concatenate the pdb
        # files together. Unfortunately, re-seeking into the trajectory
        # file causes this loop to be O(n^2)
        sub.run(
            ["rm", output_file_path],  # noqa: S603, S607
            check=False,
        )  # Delete output_file_path (if it exists) due to >> below.

        # First load all of the states so we can call count_states.
        pymol.cmd.load(input_3_path, "num_states")
        pymol.cmd.load_traj(input_4_path, "num_states")
        num_states = pymol.cmd.count_states("num_states")

        states = [interval * i for i in range(1, 1 + int(num_states / interval))]

        pymol.cmd.load(input_3_path, "aligned_sep")
        for idx, state in enumerate(states):
            # Now re-load each state individually.
            pymol.cmd.load_traj(
                input_4_path,
                "prod",
                state=1,
                start=state,
                stop=state,
                max=1,
            )

            pymol.cmd.select("P", f"prod and name CA and ({indices_receptor})")
            pymol.cmd.pair_fit("P", "G")

            pymol.cmd.select("N", f"prod and ({indices_receptor} or {indices_ligand})")
            pymol.cmd.save(
                f"{state}.pdb",
                "N",
                -1,
            )  # 0 == all states (default -1 == current state only)

            # For interactive visualization / comparison, load the aligned results.
            pymol.cmd.save(
                "temp.pdb",
                "prod",
                -1,
            )  # 0 == all states (default -1 == current state only)
            pymol.cmd.load_traj("temp.pdb", "aligned_sep", state=1 + idx)  # 0 = append
            sub.run(["rm", "temp.pdb"], check=False)  # noqa: S603, S607

            # Now concatenate the individual pdb files into output_file_path
            # TODO: For security, avoid using shell=True
            sub.run(
                f"cat {state}.pdb >> {output_file_path}",
                shell=False,  # noqa: S603
                check=True,
            )
            sub.run(["rm", f"{state}.pdb"], check=False)  # noqa: S603, S607

        # For interactive visualization / comparison, load the aligned results.

    align_averaged = True
    if align_averaged:
        # Load all of the states.
        pymol.cmd.load_traj(input_4_path, "prod", interval=interval)

        pymol.cmd.select("P", f"prod and name CA and ({indices_receptor})")
        pymol.cmd.pair_fit("P", "G")

        pymol.cmd.select("N", f"prod and ({indices_receptor} or {indices_ligand})")
        pymol.cmd.save(
            output_file_path,
            "N",
            0,
        )  # 0 == all states (default -1 == current state only)

    mdtraj = True
    if mdtraj:
        import MDAnalysis
        from MDAnalysis.analysis import align
        from MDAnalysis.coordinates import TRR

        gro = MDAnalysis.Universe(topology=input_3_path, coordinates=input_3_path)
        print(gro)  # noqa: T201
        # NOTE: Setting coordinates= in the constructor only loads the first frame!
        trr = MDAnalysis.Universe(topology=input_3_path)
        trr.trajectory = TRR.TRRReader(input_4_path)  # This loads all frames.
        print(trr)  # noqa: T201

        # Don't forget to call .run()! Otherwise, it will silently do nothing
        # (except write an empty file).
        aligntraj = align.AlignTraj(
            trr,
            gro,
            select="protein and name CA",
            filename="aligned.trr",
        ).run()
        print(aligntraj.frames)  # noqa: T201

        pymol.cmd.load(input_3_path, "aligned_mda")
        pymol.cmd.load_traj("aligned.trr", "aligned_mda")
