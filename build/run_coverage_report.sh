#!/bin/bash

use_strict_coverage=${1:-false}

is_coverage_installed_command="pip list | grep coverage"
is_coverage_installed_result=$(${is_coverage_installed_command})
#installed_coverage_version=$("${is_coverage_installed_result}" | sed 's/^coverage\s*//')

if [ "${is_coverage_installed_result}" == "" ]; then
  echo "INSTALLING COVERAGE..."
  coverage_install_command="pip install coverage"
  coverage_install_result=$(${coverage_install_command})
  coverage_install_message="*Requirement already satisfied: coverage in*"
  if [[ ${coverage_install_result} == ${coverage_install_message} ]]; then
    echo ${coverage_install_command}": SUCCESS"
  else
    echo ${coverage_install_command}": FAIL"
  fi
fi

# TODO: had to add this path to my PATH manually: C:\Users\{user}\AppData\Roaming\Python\Python39\Scripts
coverage run -m unittest discover ./tests

if [ "${use_strict_coverage}" == true ]; then
  coverage report --show-missing --no-skip-covered --rcfile=../.coveragerc --omit="tests\*,src\data\*" > ../.coverage-report-strict 2>&1
else
  coverage report --show-missing --no-skip-covered --rcfile=../.coveragerc > ../.coverage-report 2>&1
fi
