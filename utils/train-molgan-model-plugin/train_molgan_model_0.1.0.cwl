#!/usr/bin/env cwl-runner
cwlVersion: v1.0

class: CommandLineTool

label: MolGAN tool for generating small molecules

baseCommand: ["python", "/MolGAN/example.py"]

hints:
  DockerRequirement:
    dockerPull: polusai/molgan-tool@sha256:e008e74170be12dcf50a936a417b8c330ccdebf7fe17abaa8fa2689dac210725
inputs:
  input_data_path:
    label: Path to the input data file
    doc: |-
      Path to the input data file
      Type: File
      File type: input
      Accepted formats: pkl
      Example file: https://github.com/bioexcel/biobb_ml/raw/master/biobb_ml/test/reference/classification/ref_output_model_support_vector_machine.pkl
    type: File
    format: edam:format_3653
    inputBinding:
      prefix: --input_data_path

  input_NP_Score_path:
    label: Output ceout file (AMBER ceout)
    doc: |-
      Output ceout file (AMBER ceout)
      Type: File
      File type: input
      Accepted formats: gz
      Example file: https://github.com/bioexcel/biobb_amber/raw/master/biobb_amber/test/data/cphstats/sander.ceout.gz
    type: File
    format: edam:format_3987
    inputBinding:
      prefix: --input_NP_Score_path

  input_SA_Score_path:
    label: Output ceout file (AMBER ceout)
    doc: |-
      Output ceout file (AMBER ceout)
      Type: File
      File type: input
      Accepted formats: gz
      Example file: https://github.com/bioexcel/biobb_amber/raw/master/biobb_amber/test/data/cphstats/sander.ceout.gz
    type: File
    format: edam:format_3987
    inputBinding:
      prefix: --input_SA_Score_path

  output_log_path:
    label: Path to the log file
    doc: |-
      Path to the log file
      Type: string
      File type: output
      Accepted formats: log
    type: string
    format:
    - edam:format_2330
    inputBinding:
      prefix: --output_log_path
    default: system.log

  output_model_dir:
    label: Path to the output model directory
    doc: |-
      Path to the output model directory
    type: string
    format:
    - edam:format_2330 # 'Textual format'
    inputBinding:
      prefix: --output_model_dir
    default: output

  validation_metrics:
    label: The metrics are used during validation and testing. Metrics, 'np,logp,sas,qed,novelty,dc,unique,diversity,validity'
    doc: |-
      The metrics are used during validation and testing
    type: string?
    format:
    - edam:format_2330
    inputBinding:
      prefix: --validation_metrics
    default: 'np,logp,sas,qed,novelty,dc,unique,diversity,validity'

  num_epochs:
    label: The number of training epochs
    doc: |-
      The number of training epochs
      Type: int
    type: int?
    format:
    - edam:format_2330
    inputBinding:
      prefix: --num_epochs

  save_frequency:
    label: The frequency to save the outputs
    doc: |-
      The frequency to save the outputs
      Type: int
    type: int?
    format:
    - edam:format_2330
    inputBinding:
      prefix: --save_frequency

outputs:

  output_log_path:
    label: Path to the log file
    doc: |-
      Path to the log file
    type: File
    outputBinding:
      glob: $(inputs.output_log_path)
    format: edam:format_2330

  output_model_dir:
    label: Path to the output model directory
    doc: |-
      Path to the output model directory
    type: Directory
    outputBinding:
      glob: $(inputs.output_model_dir)
    format: edam:format_2330 # 'Textual format

$namespaces:
  edam: https://edamontology.org/

$schemas:
- https://raw.githubusercontent.com/edamontology/edamontology/master/EDAM_dev.owl
