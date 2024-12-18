#!/bin/bash

version=$(<VERSION)
docker build . -t polusai/load-trained-molgan-model-tool:${version}
