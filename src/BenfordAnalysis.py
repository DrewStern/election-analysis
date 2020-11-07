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

def write_benford_distribution(benford_distribution):
    output_path = get_result_output_path()
    with open(output_path, 'w') as csvfile:
        csvfile.write("YEAR,CANDIDATE,ONES,TWOS,THREES,FOURS,FIVES,SIXES,SEVENS,EIGHTS,NINES" + os.linesep)
        for year_candidate_votes in benford_distribution:
            # csvfile.write(year_candidate_votes.)
            csvfile.writelines(benford_distribution)
        csvfile.close()

def get_benford_distribution():
    # basic structure is nested dictionaries: <year, <candidate, votes>>
    candidates_by_year = dict()
    vote_count_by_candidate = dict()
    benford_distribution_by_candidate = dict()

    election_results = get_election_results()
    for election_result in election_results:
        if not candidates_by_year.get(election_result.year):
            candidates_by_year[election_result.year] = vote_count_by_candidate
        vote_count_by_candidate = partition_votes_by_leading_digit(election_results, election_result.candidate, election_result.year)
        benford_distribution_by_candidate = calculate_benford_distribution(vote_count_by_candidate, election_result.totalvotes)
        candidates_by_year[election_result.year] = benford_distribution_by_candidate

    return candidates_by_year

def calculate_benford_distribution(vote_count_by_candidate, totalvotes):
    return [100 * int(x) / int(totalvotes) for x in vote_count_by_candidate]

def partition_votes_by_leading_digit(election_results, candidate, year):
    occurrences = 9 * [0]
    for range_leading_digit in range(1, 9):
        for result in election_results:
            if result.candidate == candidate and result.year == year:
                vote_leading_digit = result.candidatevotes[0]
                occurrences[int(vote_leading_digit) - 1] += 1
    return occurrences

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

write_benford_distribution(get_benford_distribution())
