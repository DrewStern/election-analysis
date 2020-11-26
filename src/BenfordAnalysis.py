import csv
import os
from pathlib import Path
import datetime

class ElectionResult:
    def __init__(self, data):
        self.year = data[0]
        self.state = data[1]
        self.candidate = data[2].replace(",", "")
        self.party = data[3]
        self.candidatevotes = data[4]
        self.totalvotes = data[5]
        if len(data) > 6:
            self.county = data[6]

    def __str__(self):
        return "year: " + self.year + "," + "state: " + self.state + "," + "candidate: " + self.candidate + "," + "candidatevotes: " + self.candidatevotes

def write_benford_distributions(benford_distributions):
    output_path = get_result_output_path()
    with open(output_path, 'w') as csvfile:
        csvfile.write("YEAR,CANDIDATE,ONES,TWOS,THREES,FOURS,FIVES,SIXES,SEVENS,EIGHTS,NINES\n")
        for outer_key in benford_distributions:
            candidate_benford_distributions = benford_distributions[outer_key]
            for inner_key in candidate_benford_distributions:
                benford_distribution = candidate_benford_distributions[inner_key]
                csvfile.write(outer_key + ",'" + inner_key + "'," + ",".join(map(str, benford_distribution)) + "\n")
        csvfile.close()

def calculate_benford_distributions(election_results):
    return calculate_leading_digit_proportions(sum_votes_by_leading_digit(election_results))

def calculate_leading_digit_proportions(raw_vote_distribution):
    benford_distribution = dict()
    for year in raw_vote_distribution.keys():
        benford_distribution[year] = dict()
        for candidate in raw_vote_distribution[year].keys():
            sum_of_all_leading_digit_counts = sum(raw_vote_distribution[year][candidate])
            benford_distribution[year][candidate] = [100 * int(x) / int(sum_of_all_leading_digit_counts) for x in raw_vote_distribution[year][candidate]]
    return benford_distribution

def sum_votes_by_leading_digit(election_results):
    # basic structure of the data is nested dictionary: <year, <candidate, [benford_distribution]>>
    raw_vote_distribution = dict()
    for election_result in election_results:
        if not raw_vote_distribution.get(election_result.year):
            raw_vote_distribution[election_result.year] = dict()

        if not raw_vote_distribution.get(election_result.year).get(election_result.candidate):
            raw_vote_distribution[election_result.year][election_result.candidate] = 9 * [0]

        leading_digit = int(election_result.candidatevotes[0])
        raw_vote_distribution[election_result.year][election_result.candidate][leading_digit - 1] += 1
    return raw_vote_distribution

def get_election_results(data_file_path):
    with open(data_file_path) as csvfile:
        raw_data = csv.reader(csvfile)
        election_results = []
        for row in raw_data:
            election_result = ElectionResult(row)
            if not election_result.candidate:
                continue

            if election_result.candidatevotes == "NA":
                continue

            election_results.append(election_result)
        csvfile.close()
        election_results.pop(0) #remove the header row
        return election_results

def get_result_output_path():
    return get_results_directory() + "run-" + str(datetime.datetime.now()).replace(" ", "-").replace(":", "-") + ".csv"

def read_presidential_votes_state_data():
    return get_resources_directory() + "presidential-votes-by-state-1976-2016-reduced.csv"

def read_presidential_votes_county_data():
    return get_resources_directory() + "presidential-votes-by-county-2000-2016-reduced.csv"

def get_results_directory():
    return get_root_directory() + "results\\"

def get_resources_directory():
    return get_root_directory() + "resources\\"

def get_root_directory():
    return str(Path(os.path.realpath(__file__)).parent.parent) + "\\"

def find_counties_predictive_of_winner(prediction_rate_by_county):
    return [county for county in prediction_rate_by_county if prediction_rate_by_county[county] == 1]

def find_counties_predictive_of_loser(prediction_rate_by_county):
    return [county for county in prediction_rate_by_county if prediction_rate_by_county[county] == 0]

def get_prediction_rate_by_county(candidate_votes_by_year_county):
    correct_predictions_by_county = dict()
    for year in candidate_votes_by_year_county:
        for county_prediction_result in candidate_votes_by_year_county[year]:
            county_winner = None
            for candidate_result in candidate_votes_by_year_county[year][county_prediction_result].items():
                if county_winner is None:
                    county_winner = candidate_result
                if candidate_result[1] > county_winner[1]:
                    county_winner = candidate_result
            if correct_predictions_by_county.get(county_prediction_result) is None:
                correct_predictions_by_county[county_prediction_result] = 0
            if county_winner[0] in get_nationally_winning_candidates_by_year().values():
                correct_predictions_by_county[county_prediction_result] += 1
    number_of_elections = len(candidate_votes_by_year_county.keys())

    prediction_rate_by_county = dict()
    for county_prediction_result in correct_predictions_by_county.items():
        prediction_rate_by_county[county_prediction_result[0]] = county_prediction_result[1] / number_of_elections
    return prediction_rate_by_county

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

def get_nationally_winning_candidates_by_year():
    nationally_winning_candidates_by_year = dict()
    nationally_winning_candidates_by_year["2000"] = "George W. Bush"
    nationally_winning_candidates_by_year["2004"] = "George W. Bush"
    nationally_winning_candidates_by_year["2008"] = "Barack Obama"
    nationally_winning_candidates_by_year["2012"] = "Barack Obama"
    nationally_winning_candidates_by_year["2016"] = "Donald Trump"
    return nationally_winning_candidates_by_year

def get_nationally_losing_candidates_by_year():
    nationally_losing_candidates_by_year = dict()
    nationally_losing_candidates_by_year["2000"] = "Al Gore"
    nationally_losing_candidates_by_year["2004"] = "John Kerry"
    nationally_losing_candidates_by_year["2008"] = "John McCain"
    nationally_losing_candidates_by_year["2012"] = "Mitt Romney"
    nationally_losing_candidates_by_year["2016"] = "Hillary Clinton"
    return nationally_losing_candidates_by_year

# write_benford_distributions(calculate_benford_distributions(get_election_results(read_presidential_votes_state_data())))
print(find_counties_predictive_of_winner(get_prediction_rate_by_county(get_election_results_by_county(get_election_results(read_presidential_votes_county_data())))))
# print(find_counties_predictive_of_loser(get_prediction_rate_by_county(get_election_results_by_county(get_election_results(read_presidential_votes_county_data())))))
