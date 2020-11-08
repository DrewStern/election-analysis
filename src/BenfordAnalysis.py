import csv
# import ElectionResult
import numpy
# import pyplot
import os
from pathlib import Path
import datetime

class ElectionResult:
    def __init__(self, data):
        self.year = data[0]
        self.state = data[1]
        self.candidate = data[2].replace(",", "")
        self.party = data[3]
        # self.writein = data[4]
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
        for year in benford_distributions:
            candidate_benford_distributions = benford_distributions[year]
            for candidate in candidate_benford_distributions:
                benford_distribution = candidate_benford_distributions[candidate]
                csvfile.write(year + ",'" + candidate + "'," + ",".join(map(str, benford_distribution)) + "\n")
        csvfile.close()

def calculate_benford_distributions(election_results):
    # basic structure of the data is nested dictionary: <year, <candidate, [benford_distribution]>>
    benford_distributions = dict()
    leading_digit_occurrence_placeholder = 9 * [0]

    for election_result in election_results:
        # ignore cases where the candidate field is empty
        if not election_result.candidate:
            continue

        # ignore cases where candidatevotes are missing from the county-level data
        if election_result.candidatevotes == "NA":
            continue

        # add the year as the primary key
        if not benford_distributions.get(election_result.year):
            benford_distributions[election_result.year] = dict()

        # add the candidate as the secondary key
        if not benford_distributions.get(election_result.year).get(election_result.candidate):
            benford_distributions[election_result.year][election_result.candidate] = leading_digit_occurrence_placeholder

        # calculate the benford distribution
        leading_digit = int(election_result.candidatevotes[0])
        benford_distributions[election_result.year][election_result.candidate][leading_digit - 1] += 1
        benford_distributions[election_result.year][election_result.candidate] = [100 * int(x) / int(election_result.totalvotes) for x in leading_digit_occurrence_placeholder]
    return benford_distributions

def get_election_results(data_file_path):
    with open(data_file_path) as csvfile:
        raw_data = csv.reader(csvfile)
        results = []
        for row in raw_data:
            results.append(ElectionResult(row))
        csvfile.close()
        results.pop(0) #remove the header row
        return results

def get_result_output_path():
    return get_root_directory() + "\\results\\run-" + str(datetime.datetime.now()).replace(" ", "-").replace(":", "-") + ".csv"

def read_presidential_votes_state_data():
    return get_root_directory() + "\\resources\\presidential-votes-by-state-1976-2016-reduced.csv"

def read_presidential_votes_county_data():
    return get_root_directory() + "\\resources\\presidential-votes-by-county-2000-2016-reduced.csv"

def get_root_directory():
    return str(Path(os.path.realpath(__file__)).parent.parent)

write_benford_distributions(calculate_benford_distributions(get_election_results(read_presidential_votes_county_data())))
