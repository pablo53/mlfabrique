#!/bin/sh

mkdir -p build
cp ../src/dist/nnmodel-*.whl build
docker build --tag mlfabrique-nnloader:latest -f Dockerfile.nnloader .
rm -r -f build
