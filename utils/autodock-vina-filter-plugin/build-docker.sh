#!/bin/bash

version=$(<VERSION)
docker build . -t polusai/autodock-vina-filter-tool:${version}
