#!/usr/bin/env cwl-runner
cwlVersion: v1.0

class: CommandLineTool

label: Replace a column in one file with a column from another using AWKK

doc: |
  Replace a column in one file with a column from another using AWK

baseCommand: ["bash", "/replace_first_column.sh"]

hints:
  DockerRequirement:
    dockerPull: ndonyapour/replace_first_column

inputs:
  input_xvg1_path:
    label: Path to the first XVG file
    doc: |-
      Path to the first XVG file
    type: File
    format: edam:format_2030
    inputBinding:
      position: 1

  input_xvg2_path:
    label: Path to the second XVG file
    doc: |-
      Path to the second XVG file
    type: File
    format: edam:format_2030
    inputBinding:
      position: 2

  output_xvg_path:
    label: Path to the output XVG file
    doc: |-
      Path to the output XVG file
    type: string
    format: edam:format_2030
    default: system.xvg

outputs:
  output_xvg_path:
    label: Path to the output XVG file
    doc: |-
      Path to the output XVG file
    type: File
    format: edam:format_2030
    streamable: true
    outputBinding:
      glob: $(inputs.output_xvg_path)

stdout: $(inputs.output_xvg_path)

$namespaces:
  edam: https://edamontology.org/

$schemas:
- https://raw.githubusercontent.com/edamontology/edamontology/master/EDAM_dev.owl
