#!/usr/bin/env cwl-runner
cwlVersion: v1.0

class: CommandLineTool

label: Align Protein and CA atoms for a trajectory using Pymol

doc: |-
  Align Protein and CA atoms for a trajectory using Pymol

baseCommand: ["conda", "run", "-n", "project_env", "pymol"]
arguments: ["-rcQ", "/opt/executables/src/polus/mm/utils/pymol_align_protein_ca/__main__.py ", "--"]
# NOTE: Based on the last example here
# See https://pymolwiki.org/index.php/Command_Line_Options

hints:
  DockerRequirement:
    dockerPull: polusai/pymol-align-protein-ca-tool@sha256:3d51e1e6cd560b64b33159e153b68560b00701ac81307bce259dbf8d454395fd

inputs:
  input_1_path:
    label: Input receptor file path
    doc: |-
      Input receptor file path
    type: File
    format: edam:format_1476, edam:format_3877 # pdb, xyz
    inputBinding:
      prefix: --input_1_path

  input_2_path:
    label: Input ligand file path
    doc: |-
      Input ligand file path
    type: File
    format: edam:format_1476, edam:format_3877 # pdb, xyz
    inputBinding:
      prefix: --input_2_path

  input_3_path:
    label: Input structure file path
    doc: |-
      Input structure file path
    type: File
    format: edam:format_2033 # Gromacs structure *.gro
    inputBinding:
      prefix: --input_3_path

  input_4_path:
    label: Input trajectory file path
    doc: |-
      Input trajectory file path
    type: File
    format: edam:format_3910 # Gromacs trajectory *.trr
    inputBinding:
      prefix: --input_4_path

  output_file_path:
    label: Path to the output file
    doc: |-
      Path to the output file
    type: string
    format:
    - edam:format_1476 # pdb
    inputBinding:
      prefix: --output_file_path
    default: system.pdb


outputs:
  output_file_path:
    label: Path to the output file
    doc: |-
      Path to the output file
    type: File
    format: edam:format_1476 # pdb
    outputBinding:
      glob: $(inputs.output_file_path)

$namespaces:
  edam: https://edamontology.org/

$schemas:
- https://raw.githubusercontent.com/edamontology/edamontology/master/EDAM_dev.owl
