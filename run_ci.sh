#!/bin/bash

python_version=${1:-3.9.4}
pyenv_version=${2:-2.64.8}

python -m pip install --upgrade pip
pip install --upgrade -r ../requirements.txt
./build/setup_pyenv_local.sh ${python_version}
./build/run_coverage_report.sh