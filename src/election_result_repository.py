import csv
from src.election_result import ElectionResult


class ElectionResultRepository:
    def get_election_results(self, data_file_path):
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
            election_results.pop(0)  # remove the header row
            return election_results

    def get_nationally_winning_candidates_by_year(self):
        nationally_winning_candidates_by_year = dict()
        nationally_winning_candidates_by_year["2000"] = "George W. Bush"
        nationally_winning_candidates_by_year["2004"] = "George W. Bush"
        nationally_winning_candidates_by_year["2008"] = "Barack Obama"
        nationally_winning_candidates_by_year["2012"] = "Barack Obama"
        nationally_winning_candidates_by_year["2016"] = "Donald Trump"
        return nationally_winning_candidates_by_year

    def get_nationally_losing_candidates_by_year(self):
        nationally_losing_candidates_by_year = dict()
        nationally_losing_candidates_by_year["2000"] = "Al Gore"
        nationally_losing_candidates_by_year["2004"] = "John Kerry"
        nationally_losing_candidates_by_year["2008"] = "John McCain"
        nationally_losing_candidates_by_year["2012"] = "Mitt Romney"
        nationally_losing_candidates_by_year["2016"] = "Hillary Clinton"
        return nationally_losing_candidates_by_year