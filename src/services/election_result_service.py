from functools import reduce

from src.repositories.election_result_repository import ElectionResultRepository


class ElectionResultService:
    def __init__(self, election_result_repository: ElectionResultRepository):
        self.election_result_repository = election_result_repository

    def get_election_winner(self, year, county, state):
        election_ranking = self.get_election_ranking(year, county, state)
        return election_ranking[0] if len(election_ranking) > 0 else "Unknown"

    def get_election_ranking(self, year, county, state):
        unordered_election_results = self.get_election_results(year_filter=year, county_filter=county, state_filter=state)
        ordered_election_results = sorted(unordered_election_results, key=lambda x: int(x.candidatevotes), reverse=True)
        return list(map(lambda x: x.candidate, ordered_election_results))

    def get_election_years(self):
        return list(sorted(set(map(lambda x: x.year, self.get_election_results()))))

    def get_election_results(self, year_filter=None, county_filter=None, state_filter=None, candidate_filter=None, party_filter=None):
        filtered_results = []
        for election_result in self.election_result_repository.get_election_results():
            if election_result.is_not_valid():
                continue
            if election_result.is_not_major_party():
                continue
            if year_filter is not None and year_filter != election_result.year:
                continue
            if county_filter is not None and county_filter != election_result.county:
                continue
            if state_filter is not None and state_filter != election_result.state:
                continue
            if candidate_filter is not None and candidate_filter != election_result.candidate:
                continue
            if party_filter is not None and party_filter != election_result.party:
                continue
            filtered_results.append(election_result)
        return filtered_results

    def get_nationally_winning_candidate_by_year(self, year):
        winners_by_year = self.election_result_repository.get_nationally_winning_candidates_by_year()
        return winners_by_year[year] if year in winners_by_year.keys() else "Unknown"

    def get_nationally_losing_candidate_by_year(self, year):
        losers_by_year = self.election_result_repository.get_nationally_losing_candidates_by_year()
        return losers_by_year[year] if year in losers_by_year.keys() else "Unknown"
