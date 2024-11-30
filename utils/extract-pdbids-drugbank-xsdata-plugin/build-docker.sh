#!/bin/bash

version=$(<VERSION)
docker build . -t polusai/extract-pdbids-drugbank-xsdata-tool:${version}
