from src.data.models.election_event import ElectionEvent
from src.data.repositories.election_result_repository import ElectionResultRepository

class ElectionResultService:
    def __init__(self, election_result_repository: ElectionResultRepository):
        self.election_result_repository = election_result_repository

    def get_counties_won_by_party(self, year_filter, state_filter, party_filter):
        counties_won_by_party = []
        counties_in_state = self.get_counties_for_state(state_filter)
        for county in counties_in_state:
            election_event = ElectionEvent(year_filter, state_filter, county)
            winning_party = self.election_result_service.get_winning_party_for_election(election_event)
            if winning_party == party_filter:
                counties_won_by_party.append(county)
        return counties_won_by_party

    def get_winning_party_for_election(self, election_event: ElectionEvent):
        election_ranking = self.get_party_ranking_for_election(election_event)
        return election_ranking[0] if len(election_ranking) > 0 else None

    def get_party_ranking_for_election(self, election_event: ElectionEvent):
        return list(map(lambda x: x.party, self.get_ranked_election_results(election_event)))

    def get_winning_candidate_for_election(self, election_event: ElectionEvent):
        election_ranking = self.get_candidate_ranking_for_election(election_event)
        return election_ranking[0] if len(election_ranking) > 0 else None

    def get_candidate_ranking_for_election(self, election_event: ElectionEvent):
        return list(map(lambda x: x.candidate, self.get_ranked_election_results(election_event)))

    def get_ranked_election_results(self, election_event: ElectionEvent):
        unsorted_results = self.get_election_results(year_filter=election_event.year, county_filter=election_event.county, state_filter=election_event.state)
        return sorted(unsorted_results, key=lambda x: int(x.candidatevotes), reverse=True)

    def get_election_results(self, year_filter=None, county_filter=None, state_filter=None, candidate_filter=None, party_filter=None):
        filtered_results = []
        unfiltered_results = self.election_result_repository.get_election_results()
        for election_result in unfiltered_results:
            if election_result.is_not_valid():
                continue
            if election_result.is_not_major_party():
                continue
            if year_filter is not None and year_filter.lower() != election_result.year.lower():
                continue
            if county_filter is not None and county_filter.lower() != election_result.county.lower():
                continue
            if state_filter is not None and state_filter.lower() != election_result.state.lower():
                continue
            if candidate_filter is not None and candidate_filter.lower() != election_result.candidate.lower():
                continue
            if party_filter is not None and party_filter.lower() != election_result.party.lower():
                continue
            filtered_results.append(election_result)
        return filtered_results

    def get_nationally_winning_candidate_by_year(self, year):
        winners_by_year = self.election_result_repository.get_nationally_winning_candidates_by_year()
        return winners_by_year[year] if year in winners_by_year.keys() else None

    def get_nationally_losing_candidate_by_year(self, year):
        losers_by_year = self.election_result_repository.get_nationally_losing_candidates_by_year()
        return losers_by_year[year] if year in losers_by_year.keys() else None
