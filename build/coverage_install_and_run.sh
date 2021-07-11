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

# TODO: still need to trim some extra white lines out of the output here
coverage report -m | sed 's/^.*__init__.*$//' | cat -s

#$ coverage run -m unittest discover ./tests && coverage report -m | sed 's/^.*__init__.*$//' | cat -s
#Name                                                       Stmts   Miss  Cover   Missing
#----------------------------------------------------------------------------------------
#
#src\data\models\election_event.py                             11      2    82%   10, 13
#src\data\models\election_result.py                            23      1    96%   19
#
#src\data\repositories\election_result_repository.py           33     17    48%   13, 23-30, 33-40
#src\data\repositories\mock_election_result_repository.py      19      6    68%   55-60
#
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
