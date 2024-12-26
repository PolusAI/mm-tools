#!/bin/bash

version=$(<VERSION)
docker build . -t polusai/pymol-align-protein-ca-tool:${version}
