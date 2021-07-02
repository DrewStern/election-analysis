from src.services.election_result_service import ElectionResultService


class ElectionEventService:
    def __init__(self, election_result_service: ElectionResultService):
        self.election_result_service = election_result_service

    def get_counties_won_by_party(self, year_filter, state_filter, party_filter):
        counties_won_by_party = []
        counties_in_state = self.get_counties_for_state(state_filter)
        for county in counties_in_state:
            winning_party = self.election_result_service.get_winning_party_for_election(year_filter, county, state_filter)
            if winning_party == party_filter:
                counties_won_by_party.append(county)
        return counties_won_by_party

    def get_counties_for_state(self, state):
        return list(sorted(set(map(lambda x: x.county, self.election_result_service.get_election_results(state_filter=state)))))

    def get_localities(self):
        return list(sorted(set(map(lambda x: x.locale, self.election_result_service.get_election_results()))))