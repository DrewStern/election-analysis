import datetime
import os
from pathlib import Path

from src.benford_analysis_service import BenfordAnalysisService
from src.election_result_repository import ElectionResultRepository
from src.predictiveness_analysis_service import PredictivenessAnalysisService


def write_predictiveness_analysis(get_prediction_rate_by_county, output_path):
    with open(output_path, 'w') as csvfile:
        csvfile.write("COUNTY,PREDICTION_RATE\n")
        for prediction_rate_by_county in get_prediction_rate_by_county.items():
            csvfile.write(prediction_rate_by_county[0] + "," + str(prediction_rate_by_county[1]) + "\n")
        csvfile.close()


def write_benford_analysis(benford_distributions, output_path):
    with open(output_path, 'w') as csvfile:
        csvfile.write("YEAR,CANDIDATE,ONES,TWOS,THREES,FOURS,FIVES,SIXES,SEVENS,EIGHTS,NINES\n")
        for outer_key in benford_distributions:
            candidate_benford_distributions = benford_distributions[outer_key]
            for inner_key in candidate_benford_distributions:
                benford_distribution = candidate_benford_distributions[inner_key]
                csvfile.write(outer_key + ",'" + inner_key + "'," + ",".join(map(str, benford_distribution)) + "\n")
        csvfile.close()


def get_result_output_path():
    return get_results_directory() + "run-" + str(datetime.datetime.now()).replace(" ", "-").replace(":", "-") + ".csv"


def get_results_directory():
    return get_resources_directory() + "results\\"


def read_presidential_votes_state_data_new():
    return get_resources_directory() + "working_data\\presidential-votes-by-state-1976-2020-working.csv"


def read_presidential_votes_state_data_old():
    return get_resources_directory() + "working_data\\presidential-votes-by-state-1976-2016-working.csv"


def read_presidential_votes_county_data():
    return get_resources_directory() + "working_data\\presidential-votes-by-county-2000-2016-working.csv"


def get_resources_directory():
    return get_root_directory() + "resources\\"


def get_root_directory():
    return str(Path(os.path.realpath(__file__)).parent.parent) + "\\"


election_result_repository = ElectionResultRepository()
county_level_results = election_result_repository.get_election_results_by_county(election_result_repository.get_election_results(read_presidential_votes_county_data()))

benfordAnalysisService = BenfordAnalysisService()
benford_distribution = benfordAnalysisService.calculate_benford_distribution(county_level_results)
write_benford_analysis(benford_distribution, get_result_output_path())

predictivenessAnalysisService = PredictivenessAnalysisService(election_result_repository)
predictiveness_results = predictivenessAnalysisService.get_prediction_rate_by_county(county_level_results)
write_predictiveness_analysis(predictiveness_results, get_result_output_path())
