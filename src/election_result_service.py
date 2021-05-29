from src.election_result_repository import ElectionResultRepository


class ElectionResultService:
    def __init__(self, election_result_repository: ElectionResultRepository):
        self.election_result_repository = election_result_repository

    def get_election_winner(self, year, county, state):
        election_ranking = self.get_election_ranking(year, county, state)
        return election_ranking[0] if len(election_ranking) > 0 else "Unknown"

    def get_election_ranking(self, year, county, state):
        election_ranking = []
        for election_result in self.get_election_results():
            if election_result.is_from_election(year, county, state):
                election_ranking.append(election_result)
        return list(map(lambda x: x.candidate, sorted(election_ranking, key=lambda x: int(x.candidatevotes), reverse=True)))

    def get_election_years(self):
        election_years = []
        for election_result in self.get_election_results():
            if election_result.year not in election_years:
                election_years.append(election_result.year)
        return election_years

    def get_election_results(self, only_valid_results=True, only_major_party_results=True):
        filtered_results = []
        for election_result in self.election_result_repository.get_election_results():
            if only_valid_results and election_result.is_not_valid():
                continue
            if only_major_party_results and election_result.is_not_major_party():
                continue
            filtered_results.append(election_result)
        return filtered_results

    def get_nationally_winning_candidate_by_year(self, year):
        winners_by_year = self.election_result_repository.get_nationally_winning_candidates_by_year()
        return winners_by_year[year] if year in winners_by_year.keys() else "Unknown"

    def get_nationally_winning_candidates_by_year(self):
        return self.election_result_repository.get_nationally_winning_candidates_by_year()

    def get_nationally_losing_candidate_by_year(self, year):
        losers_by_year = self.election_result_repository.get_nationally_losing_candidates_by_year()
        return losers_by_year[year] if year in losers_by_year.keys() else "Unknown"

    def get_nationally_losing_candidates_by_year(self):
        return self.election_result_repository.get_nationally_losing_candidates_by_year()
