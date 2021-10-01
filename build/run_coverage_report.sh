#!/bin/bash

use_strict_coverage=${1:-false}

coverage run -m unittest discover ./tests

if [ ${use_strict_coverage} == true ]; then
  coverage report --show-missing --no-skip-covered --rcfile=./.coveragerc --omit="tests\*,src\data\*" > ./.coverage-report-strict 2>&1
else
  coverage report --show-missing --no-skip-covered --rcfile=./.coveragerc > ./.coverage-report 2>&1
fi
