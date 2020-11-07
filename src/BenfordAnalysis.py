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
        self.candidate = data[2]
        self.party = data[3]
        self.writein = data[4]
        self.candidatevotes = data[5]
        self.totalvotes = data[6]

    def __str__(self):
        return "year: " + self.year + "," + "state: " + self.state + "," + "candidate: " + self.candidate + "," + "candidatevotes: " + self.candidatevotes

def write_benford_distributions(benford_distributions):
    output_path = get_result_output_path()
    with open(output_path, 'w') as csvfile:
        csvfile.write("YEAR,CANDIDATE,ONES,TWOS,THREES,FOURS,FIVES,SIXES,SEVENS,EIGHTS,NINES" + os.linesep)
        for benford_distribution in benford_distributions:
            csvfile.write(benford_distribution)
        csvfile.close()

def calculate_benford_distribution():
    # basic structure of the data is nested dictionary: <year, <candidate, [benford_distribution]>>
    result = dict()
    occurrences = 9 * [0]
    election_results = get_election_results()

    for range_leading_digit in range(1, 9):
        for election_result in election_results:
            # add the year as the primary key
            if not result.get(election_result.year):
                result[election_result.year] = dict()

            # add the candidate as the secondary key
            if not result.get(election_result.year).get(election_result.candidate):
                result[election_result.year][election_result.candidate] = dict()

            # calculate the benford distribution
            vote_leading_digit = int(election_result.candidatevotes[0])
            occurrences[vote_leading_digit - 1] += 1
            result[election_result.year][election_result.candidate] = [int(x) / int(election_result.totalvotes) for x in occurrences]
    return result

def get_election_results():
    with open(read_presidential_votes_state_data()) as csvfile:
        raw_data = csv.reader(csvfile)
        results = []
        for row in raw_data:
            results.append(ElectionResult(row))
        csvfile.close()
        results.pop(0) #remove the header row
        return results

def get_result_output_path():
    return get_root_directory() + "\\results\\benford-distribution-" + str(datetime.datetime.now()).replace(" ", "-").replace(":", "-")

def read_presidential_votes_state_data():
    return get_root_directory() + "\\resources\\presidential-votes-by-state-1976-2016-reduced.csv"

def read_presidential_votes_county_data():
    return get_root_directory() + "\\resources\\presidential-votes-by-county-2000-2016-reduced.csv"

def get_root_directory():
    return str(Path(os.path.realpath(__file__)).parent.parent)

write_benford_distributions(calculate_benford_distribution())
