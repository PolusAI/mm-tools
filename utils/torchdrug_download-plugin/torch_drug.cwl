#!/usr/bin/env cwl-runner
cwlVersion: v1.0

class: CommandLineTool

label: Access datasets and models from TorchDrug

doc: |-
  Access datasets and models from TorchDrug

baseCommand: ["python", "-m", "polus.mm.utils.torchdrug_download"]

hints:
  DockerRequirement:
    dockerPull: mrbrandonwalker/torch_drug

inputs:

  dataset:
    label: Input dataset to extract
    doc: |-
      Input dataset to extract
    type: string
    inputBinding:
      prefix: --dataset

outputs:

  output_csv:
    label: Path to the output CSV file
    doc: |-
      Path to the output CSV file
    type: Directory
    outputBinding:
      glob: "*.csv"


$namespaces:
  edam: https://edamontology.org/

$schemas:
- https://raw.githubusercontent.com/edamontology/edamontology/master/EDAM_dev.owl
