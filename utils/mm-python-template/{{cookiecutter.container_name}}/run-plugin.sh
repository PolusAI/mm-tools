#!/bin/bash

version=$(<VERSION)

container_input_dir="/inpdir"
container_output_dir="/outdir"

docker run -v $tool_mount_path_input:/${container_input_dir} \
           -v $tool_mount_path_output:/${container_output_dir} \
            --user $(id -u):$(id -g) \