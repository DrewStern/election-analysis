#!/bin/bash

python_version=$1
pyenv_version=$2

python -m pip install --upgrade pip

pip install pyenv-win --target $HOME\\.pyenv
# TODO: test the pyenv version?
#pyenv --version
#pyenv 2.64.8
# generalizes to
#pyenv ${pyenv_version}

# update our pyenv to latest version
#pyenv update

# lists what Python versions are available for local install
# TODO: need to automate finding latest version
# pyenv install --list

# install and set the local python version
pyenv install ${python_version}
# TODO: verify installation successful by testing that last line echoes the following:
# :: [Info] :: completed! 3.9.4
# generalizes to
# :: [Info] :: completed! ${python_version}
pyenv local ${python_version}

pip install coverage

# TODO: had to add this path to my PATH manually:
# C:\Users\{user}}\AppData\Roaming\Python\Python39\Scripts
#python -m unittest discover ./tests
coverage run -m unittest discover ./tests

# TODO: doesn't seem to be discovering all of the code? most of the services are missing below?
coverage report -m
#$ coverage report -m
#Name                                                Stmts   Miss  Cover   Missing
#---------------------------------------------------------------------------------
#src\__init__.py                                         0      0   100%
#src\models\election_event.py                           11      4    64%   8-10, 13
#src\models\election_result.py                          23      1    96%   19
#src\repositories\election_result_repository.py         33     17    48%   13, 23-30, 33-40
#src\services\__init__.py                                0      0   100%
#src\services\analysis\__init__.py                       0      0   100%
#src\services\analysis\benford_analysis_service.py      31      2    94%   19, 31
#src\services\election_result_service.py                42     13    69%   9-10, 13, 16-17, 20, 23-24, 36, 47-48, 51-52
#tests\test_mit_integration.py                         721      4    99%   783, 786, 789, 808
#---------------------------------------------------------------------------------
#TOTAL                                                 861     41    95%

# TODO: these haven't actually been used anywhere yet
#pip install mock
#pip install rpy2
#pip install numpy
#pip install matplotlib