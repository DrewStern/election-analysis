import csv
# import ElectionResult
import numpy
# import pyplot

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

def write_distribution():
    with open(read_presidential_votes_state_data()) as csvfile:
        raw_data = csv.reader(csvfile)
        data_by_year = filter_by_year(raw_data, "1976")
        candidates_by_year = get_candidates(data_by_year)
        vote_distribution_by_candidate = dict()
        for candidate in candidates_by_year:
            vote_distribution_by_candidate[candidate] = calculate_candidate_vote_distribution(data_by_year, candidate)
            print(candidate + " : ")
            print(vote_distribution_by_candidate[candidate])

def calculate_candidate_vote_distribution(data, candidate):
    occurrences = 9 * [0]
    for range_leading_digit in range(1, 9):
        for row in data:
            if row.writein is True:
                continue
            if row.candidate == candidate:
                vote_leading_digit = row.candidatevotes[0]
                occurrences[int(vote_leading_digit) - 1] += 1
    return occurrences

def get_candidates(data):
    candidates = []
    for row in data:
        if row.candidate and row.candidate not in candidates:
            candidates.append(row.candidate)
    return candidates

def filter_by_year(data, year):
    return filter_by(data, 'year', year)

def filter_by(data, property_name, with_matching_value):
    meets_criteria = []
    for row in data:
        result = ElectionResult(row)
        if getattr(result, property_name) == with_matching_value:
            meets_criteria.append(result)
    return meets_criteria

def read_presidential_votes_state_data():
    return "D:\\code\\benford-analysis\\resources\\presidential-votes-by-state-1976-2016-reduced.csv"

def read_presidential_votes_county_data():
    return "D:\\code\\benford-analysis\\resources\\presidential-votes-by-county-2000-2016-reduced.csv"

write_distribution()
