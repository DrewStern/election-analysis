from src.services.election_history_service import ElectionHistoryService
from src.services.election_result_service import ElectionResultService


class LocalityResultService:
    def __init__(self, election_result_service: ElectionResultService, election_history_service: ElectionHistoryService):
        self.election_result_service = election_result_service
        self.election_history_service = election_history_service

    def get_bellwether_counties(self):
        pass

    def get_most_loyal_counties_by_party(self, party_filter):
        pass

    def get_least_loyal_counties_by_party(self, party_filter):
        pass

    def get_locality_loyalty_ranking_by_party(self):
        locality_loyalty_ranking = dict.fromkeys(self.get_localities())
        for year in self.election_history_service.get_election_years():
            for locality in self.get_localities():
                continue
        return locality_loyalty_ranking

    def get_counties_for_state(self, state):
        return list(sorted(set(map(lambda x: x.county, self.election_result_service.get_election_results(state_filter=state)))))

    def get_localities(self):
        return list(sorted(set(map(lambda x: x.locale, self.election_result_service.get_election_results()))))