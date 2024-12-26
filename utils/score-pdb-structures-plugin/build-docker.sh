#!/bin/bash

version=$(<VERSION)
docker build . -t polusai/score-pdb-structures-tool:${version}
