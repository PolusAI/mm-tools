#!/bin/bash

version=$(<VERSION)
docker build . -t polusai/extract-data-csv-plugin:${version}
