from src.services.domain.election_history_service import ElectionHistoryService


class LoyaltyService:
    def __init__(self, election_history_service: ElectionHistoryService):
        self.election_history_service = election_history_service

    def get_most_loyal_counties_by_party(self, party_filter, head_count=10):
        pass

    def get_least_loyal_counties_by_party(self, party_filter, tail_count=10):
        pass

    def get_locality_loyalty_ranking_by_party(self):
        locality_loyalty_ranking = dict.fromkeys(self.get_localities())
        for year in self.election_history_service.get_election_years():
            for locality in self.get_localities():
                continue
        return locality_loyalty_ranking