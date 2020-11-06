import csv
import ElectionResult
import numpy
# import pyplot

def write_distribution():
    with open(read_presidential_votes_state_data()) as csvfile:
        unfiltered_results = csv.reader(csvfile)
        filtered_results = filter_by_year(unfiltered_results, "1976")
        # filtered_results = filter_by_candidate(filtered_results, "Carter, Jimmy")
        distribution = calculate_distribution(filtered_results)
        print(distribution)

def calculate_distribution(data):
    occurrences = 9 * [0]
    for range_leading_digit in range(1, 9):
        for row in data:
            if row.writein is True:
                continue
            vote_leading_digit = row.candidatevotes[0]
            occurrences[int(vote_leading_digit) - 1] += 1
    return occurrences

def filter_by_candidate(data, candidate_name):
    return filter_by(data, 'candidate', candidate_name)

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
