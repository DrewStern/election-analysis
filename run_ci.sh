#!/bin/bash

# TODO: need to specify default values here
python_version=$1
pyenv_version=$2

python -m pip install --upgrade pip

./build/get_latest_poetry.sh

./build/get_latest_pyenv.sh ${pyenv_version}

./build/pyenv_local_setup.sh ${python_version}

./build/coverage_install_and_run.sh