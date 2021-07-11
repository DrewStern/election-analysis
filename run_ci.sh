#!/bin/bash

python_version=${1:-3.9.4}
pyenv_version=${2:-2.64.8}

python -m pip install --upgrade pip

./build/get_latest_poetry.sh

./build/get_latest_pyenv.sh ${pyenv_version}

./build/pyenv_local_setup.sh ${python_version}

./build/coverage_install_and_run.sh