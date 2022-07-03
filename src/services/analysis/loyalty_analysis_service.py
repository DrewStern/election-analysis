from src.services.models.election_history_service import ElectionHistoryService


class LoyaltyAnalysisService:
    def __init__(self, election_history_service: ElectionHistoryService):
        self.election_history_service = election_history_service

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