#!/bin/bash

# TODO: need to specify default values here
python_version=$1
pyenv_version=$2

python -m pip install --upgrade pip

./get_latest_poetry.sh

./get_latest_pyenv.sh ${pyenv_version}

./pyenv_local_setup.sh ${python_version}

./coverage_install_and_run.sh