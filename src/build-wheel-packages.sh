#!/bin/bash

export CONDA_BASE=$(conda info --base)

eval "$(conda shell.bash hook)"
conda activate mlfabrique-dev

python setup.py sdist bdist_wheel
