import datetime
import os
from pathlib import Path

from src.benford_analysis_service import BenfordAnalysisService
from src.election_result_repository import ElectionResultRepository
from src.predictiveness_analysis_service import PredictivenessAnalysisService


def read_presidential_votes_state_data_new():
    return get_resources_directory() + "presidential-votes-by-state-1976-2020-reduced.csv"


def read_presidential_votes_state_data_old():
    return get_resources_directory() + "presidential-votes-by-state-1976-2016-reduced.csv"


def read_presidential_votes_county_data():
    return get_resources_directory() + "presidential-votes-by-county-2000-2016-reduced.csv"


def get_resources_directory():
    return get_root_directory() + "resources\\"


def get_result_output_path():
    return get_results_directory() + "run-" + str(datetime.datetime.now()).replace(" ", "-").replace(":", "-") + ".csv"


def get_results_directory():
    return get_root_directory() + "expected_results\\"


def get_root_directory():
    return str(Path(os.path.realpath(__file__)).parent.parent) + "\\"


repository = ElectionResultRepository()
benfordAnalysisService = BenfordAnalysisService(repository)
predictivenessAnalysisService = PredictivenessAnalysisService(repository)

benfordAnalysisService.write_benford_distributions(
    benfordAnalysisService.calculate_benford_distributions(
        repository.get_election_results_by_county(repository.get_election_results(read_presidential_votes_county_data()))),
    get_result_output_path())

predictivenessAnalysisService.write_counties_by_predictiveness(
    predictivenessAnalysisService.get_prediction_rate_by_county(
        repository.get_election_results_by_county(repository.get_election_results(read_presidential_votes_county_data()))),
    get_result_output_path())
