#!/bin/bash

# TODO: need to specify default values here
python_version=$1
pyenv_version=$2

python -m pip install --upgrade pip

# update our poetry to latest version if needed
pip install --user poetry
current_poetry_version=$(poetry self update)
if [[ ${current_poetry_version} == "You are using the latest version" ]]; then
  echo "poetry self update: unnecessary"
else
  echo "poetry self update: UPDATED"
fi

pip install pyenv-win --target $HOME\\.pyenv

# update our pyenv to latest version if needed
current_pyenv_version=$(pyenv --version)
#if [[ ${current_pyenv_version} == "*${pyenv_version}*" ]]; then
if [[ ${current_pyenv_version} == "pyenv 2.64.8" ]]; then
  echo "pyenv update: unnecessary"
else
  echo "pyenv update: UPDATING..."
  pyenv update
  echo "pyenv update: UPDATED"
fi

# lists what Python versions are available for local install
# TODO: need to automate finding latest version
# pyenv install --list

# try to install then set the local python version to the user-specified value
pyenv_install_status=$(pyenv install ${python_version})
#if [[ ${pyenv_install_status} == "*completed!*${python_version}*" ]]; then
if [[ ${pyenv_install_status} == "*completed!*3.9.4*" ]]; then
  echo "pyenv install status: SUCCESS"
else
  echo "pyenv install status: FAIL"
fi

pyenv local ${python_version}

current_coverage_version=$(pip install coverage)
if [[ ${current_coverage_version} == "*Requirement already satisfied: coverage in*" ]]; then
  echo "coverage already installed"
else
  echo "coverage installing..."
  echo "coverage installed"
fi

# TODO: had to add this path to my PATH manually: C:\Users\{user}\AppData\Roaming\Python\Python39\Scripts
coverage run -m unittest discover ./tests

coverage report -m

#$ coverage run -m unittest discover ./tests && coverage report -m
#..............................................................................................
#----------------------------------------------------------------------
#Ran 94 tests in 42.216s
#
#OK
#Name                                                       Stmts   Miss  Cover   Missing
#----------------------------------------------------------------------------------------
#src\__init__.py                                                0      0   100%
#src\data\__init__.py                                           0      0   100%
#src\data\models\__init__.py                                    0      0   100%
#src\data\models\election_event.py                             11      2    82%   10, 13
#src\data\models\election_result.py                            23      1    96%   19
#src\data\repositories\__init__.py                              0      0   100%
#src\data\repositories\election_result_repository.py           33     17    48%   13, 23-30, 33-40
#src\data\repositories\mock_election_result_repository.py      19      6    68%   55-60
#src\services\__init__.py                                       0      0   100%
#src\services\analysis\__init__.py                              0      0   100%
#src\services\analysis\benford_analysis_service.py             31      2    94%   19, 31
#src\services\analysis\prediction_analysis_service.py          34      1    97%   26
#src\services\election_event_service.py                        31      0   100%
#src\services\election_history_service.py                      20      0   100%
#src\services\election_result_service.py                       42      2    95%   51-52
#tests\test_benford_analysis_service.py                        90      1    99%   136
#tests\test_election_event_service.py                          54      0   100%
#tests\test_election_history_service.py                        31      0   100%
#tests\test_election_result_service.py                         67      1    99%   90
#tests\test_mit_integration.py                                721      4    99%   783, 786, 789, 808
#tests\test_prediction_analysis_service.py                     66      1    98%   86
#----------------------------------------------------------------------------------------
#TOTAL                                                       1273     38    97%