from src.election_result_repository import ElectionResultRepository


class ElectionResultService:
    def __init__(self, election_result_repository: ElectionResultRepository):
        self.election_result_repository = election_result_repository

    def get_election_results(self, only_valid_results=True, only_major_party_results=True):
        filtered_results = []
        for election_result in self.election_result_repository.get_election_results():
            if only_valid_results and election_result.is_not_valid():
                continue
            if only_major_party_results and election_result.is_not_major_party():
                continue
            filtered_results.append(election_result)
        return filtered_results
