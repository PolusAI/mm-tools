#!/bin/bash

version=$(<VERSION)
docker build . -t polusai/extract-pdbids-drugbank-tool:${version}
