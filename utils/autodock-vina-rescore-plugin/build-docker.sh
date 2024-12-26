#!/bin/bash

version=$(<VERSION)
docker build . -t polusai/polusai/autodock-vina-tool:${version}
