#!/bin/bash

# lists what Python versions are available for local install
python_version=$1
pyenv_local_command="pyenv local"
pyenv_local_command_result=$(${pyenv_local_command})
if [[ ${pyenv_local_command_result} == ${python_version} ]]; then
  echo "using desired python version, nothing to do"
else
  # try to install then set the local python version to the user-specified value
  # pyenv install --list | grep -x "^${python_version}$"
  pyenv_install_command="pyenv install ${python_version}"
  pyenv_install_result=$(${pyenv_install_command})
  pyenv_install_message=":: [Info] :: completed! ${python_version}"
  if [[ ${pyenv_install_result} == ${pyenv_install_message} ]]; then
    echo ${pyenv_install_command}": SUCCESS"
  else
    echo ${pyenv_install_command}": FAIL"
  fi
  pyenv local ${python_version}
fi