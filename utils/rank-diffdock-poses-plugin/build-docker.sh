#!/bin/bash

version=$(<VERSION)
docker build . -t polusai/rank-diffdock-poses-plugin:${version}
