from src.election_result_service import ElectionResultService


class BenfordAnalysisService:
    def __init__(self, election_result_service: ElectionResultService):
        self.election_result_service = election_result_service

    def calculate_benford_distribution(self):
        leading_digit_occurrences = 9 * [0]
        for election_result in self.election_result_service.get_election_results():
            leading_digit = int(election_result.candidatevotes[0])
            leading_digit_occurrences[leading_digit - 1] += 1
        return [round(100 * int(x) / int(sum(leading_digit_occurrences)), 2) for x in leading_digit_occurrences]