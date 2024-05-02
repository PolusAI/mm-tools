#!/bin/bash

version=$(<VERSION)
docker build . -t polusai/combine-structure-plugin:${version}
