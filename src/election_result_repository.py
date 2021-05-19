import csv
from src.election_result import ElectionResult


class ElectionResultRepository:
    def get_election_results(self, data_file_path, major_party_results_only=True):
        with open(data_file_path) as csvfile:
            raw_data = csv.reader(csvfile)
            election_results = []
            for row in raw_data:
                election_result = ElectionResult(row)
                if not election_result.candidate:
                    continue

                if election_result.candidatevotes == "NA":
                    continue

                if major_party_results_only and election_result.is_not_major_party():
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
        nationally_winning_candidates_by_year["2020"] = "Joe Biden"
        return nationally_winning_candidates_by_year

    def get_nationally_losing_candidates_by_year(self):
        nationally_losing_candidates_by_year = dict()
        nationally_losing_candidates_by_year["2000"] = "Al Gore"
        nationally_losing_candidates_by_year["2004"] = "John Kerry"
        nationally_losing_candidates_by_year["2008"] = "John McCain"
        nationally_losing_candidates_by_year["2012"] = "Mitt Romney"
        nationally_losing_candidates_by_year["2016"] = "Hillary Clinton"
        nationally_losing_candidates_by_year["2020"] = "Donald Trump"
        return nationally_losing_candidates_by_year
