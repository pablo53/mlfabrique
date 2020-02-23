#!/bin/sh

mkdir -p build
cp ../src/dist/nnmodel-*.whl build

./docker-build.nntrainer-cpu-base.sh
./docker-build.nntrainer-gpu-base.sh
./docker-build.nntrainer-cpu.sh
./docker-build.nntrainer-gpu.sh

rm -r -f build
