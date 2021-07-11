#!/bin/bash

coverage_install_command="pip install coverage"
coverage_install_result=$(${coverage_install_command})
coverage_install_message="*Requirement already satisfied: coverage in*"
if [[ ${coverage_install_result} == ${coverage_install_message} ]]; then
  echo ${coverage_install_command}": SUCCESS"
else
  echo ${coverage_install_command}": FAIL"
fi

# TODO: had to add this path to my PATH manually: C:\Users\{user}\AppData\Roaming\Python\Python39\Scripts
coverage run -m unittest discover ./tests

coverage report -m