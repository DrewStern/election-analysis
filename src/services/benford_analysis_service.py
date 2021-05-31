from src.services.election_result_service import ElectionResultService


class BenfordAnalysisService:
    def __init__(self, election_result_service: ElectionResultService):
        self.election_result_service = election_result_service
        self.expected_distribution = [30.1, 17.6, 12.5, 9.7, 7.9, 6.7, 5.8, 5.1, 4.6]

    def calculate_benford_distribution(self):
        leading_digit_occurrences = 9 * [0]
        for election_result in self.election_result_service.get_election_results():
            leading_digit = int(election_result.candidatevotes[0])
            leading_digit_occurrences[leading_digit - 1] += 1
        return [round(100 * int(x) / int(sum(leading_digit_occurrences)), 2) for x in leading_digit_occurrences]