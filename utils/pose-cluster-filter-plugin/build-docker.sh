#!/bin/bash

version=$(<VERSION)
docker build . -t polusai/pose-cluster-filter-plugin:${version}
