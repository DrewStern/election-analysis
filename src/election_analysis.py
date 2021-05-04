import datetime
import os
from pathlib import Path

from src.election_result_repository import ElectionResultRepository
from src.predictiveness_analysis_service import PredictivenessAnalysisService


def read_presidential_votes_state_data():
    return get_resources_directory() + "presidential-votes-by-state-1976-2016-reduced.csv"

def read_presidential_votes_county_data():
    return get_resources_directory() + "presidential-votes-by-county-2000-2016-reduced.csv"

def get_resources_directory():
    return get_root_directory() + "resources\\"

def get_result_output_path():
    return get_results_directory() + "run-" + str(datetime.datetime.now()).replace(" ", "-").replace(":", "-") + ".csv"

def get_results_directory():
    return get_root_directory() + "results\\"

def get_root_directory():
    return str(Path(os.path.realpath(__file__)).parent.parent) + "\\"

def get_election_results_by_county(election_results):
    # basic structure of the data is nested dictionary: <year, <county_by_state, <candidate, vote_count>>>
    candidate_votes_by_year_county = dict()

    for election_result in election_results:
        # only care about major party candidates for now
        if election_result.party != "republican" and election_result.party != "democrat":
            continue

        county_by_state = election_result.county + "," + election_result.state

        if not candidate_votes_by_year_county.get(election_result.year):
            candidate_votes_by_year_county[election_result.year] = dict()
        if not candidate_votes_by_year_county.get(election_result.year).get(county_by_state):
            candidate_votes_by_year_county[election_result.year][county_by_state] = dict()
        if not candidate_votes_by_year_county.get(election_result.year).get(county_by_state).get(election_result.candidate):
            candidate_votes_by_year_county[election_result.year][county_by_state][election_result.candidate] = dict()

        candidate_votes_by_year_county[election_result.year][county_by_state][election_result.candidate] = election_result.candidatevotes

    return candidate_votes_by_year_county

repository = ElectionResultRepository()
predictivenessAnalysisService = PredictivenessAnalysisService(repository)
predictivenessAnalysisService.write_counties_by_predictiveness(predictivenessAnalysisService.get_prediction_rate_by_county(get_election_results_by_county(repository.get_election_results(read_presidential_votes_county_data()))))