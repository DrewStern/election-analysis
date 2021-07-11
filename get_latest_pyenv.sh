#!/bin/bash

# install pyenv and update to latest version if needed
pyenv_version=$1 #2.64.8
pyenv_command="pyenv --version"
pyenv_command_result=$(${pyenv_command})
pyenv_version_message="pyenv ${pyenv_version}"
if [[ ${pyenv_command_result} == ${pyenv_version_message} ]]; then
  echo ${pyenv_command}": ALREADY UP TO DATE"
else
  echo ${pyenv_command}": UPDATING"
  pyenv update
  echo ${pyenv_command}": UPDATED"
fi