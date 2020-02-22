#!/bin/sh

docker build --tag mlfabrique-nnloader-base:latest -f Dockerfile.nnloader-base .
docker build --tag mlfabrique-nnloader:latest -f Dockerfile.nnloader .
