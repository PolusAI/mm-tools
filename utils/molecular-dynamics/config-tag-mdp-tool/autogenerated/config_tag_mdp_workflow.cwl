#!/usr/bin/env cwl-runner
# This file was autogenerated using the Workflow Inference Compiler, version 0+unknown
# https://github.com/PolusAI/workflow-inference-compiler
steps:
- id: config_tag_mdp_workflow__step__1__config_tag_mdp_0@1@0
  in:
    config:
      source: config_tag_mdp_workflow__step__1__config_tag_mdp_0@1@0___config
    dt:
      source: config_tag_mdp_workflow__step__1__config_tag_mdp_0@1@0___dt
    nsteps:
      source: config_tag_mdp_workflow__step__1__config_tag_mdp_0@1@0___nsteps
    ref_p:
      source: config_tag_mdp_workflow__step__1__config_tag_mdp_0@1@0___ref_p
    ref_t:
      source: config_tag_mdp_workflow__step__1__config_tag_mdp_0@1@0___ref_t
  out:
  - output_config_string
  run: config_tag_mdp_workflow__step__1__config_tag_mdp_0@1@0/config_tag_mdp_0@1@0.cwl
cwlVersion: v1.2
class: Workflow
$namespaces:
  edam: https://edamontology.org/
$schemas:
- https://raw.githubusercontent.com/edamontology/edamontology/master/EDAM_dev.owl
inputs:
  config_tag_mdp_workflow__step__1__config_tag_mdp_0@1@0___config:
    type: string
    format: edam:format_2330
    label: A dictionary of the given arguments as a JSON-encoded string.
    doc: A dictionary of the given arguments as a JSON-encoded string.
  config_tag_mdp_workflow__step__1__config_tag_mdp_0@1@0___dt:
    type: float
    label: The length of each timestep
    doc: The length of each timestep
  config_tag_mdp_workflow__step__1__config_tag_mdp_0@1@0___nsteps:
    type: int
    label: The number of timesteps
    doc: The number of timesteps
  config_tag_mdp_workflow__step__1__config_tag_mdp_0@1@0___ref_p:
    type: float
    label: The nominal pressure
    doc: The nominal pressure
  config_tag_mdp_workflow__step__1__config_tag_mdp_0@1@0___ref_t:
    type: float
    label: The nominal temperature
    doc: The nominal temperature
outputs:
  config_tag_mdp_workflow__step__1__config_tag_mdp_0@1@0___output_config_string:
    type: string
    label: A dictionary of the given arguments as a JSON-encoded string.
    doc: A dictionary of the given arguments as a JSON-encoded string.
    outputSource: config_tag_mdp_workflow__step__1__config_tag_mdp_0@1@0/output_config_string
