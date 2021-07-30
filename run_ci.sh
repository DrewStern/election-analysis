#!/bin/bash

python_version=${1:-3.9.4}
pyenv_version=${2:-2.64.8}

python -m pip install --upgrade pip
./build/install_requirements.sh
./build/get_latest_poetry.sh
./build/get_latest_pyenv.sh ${pyenv_version}
./build/setup_pyenv_local.sh ${python_version}
./build/run_coverage_report.sh