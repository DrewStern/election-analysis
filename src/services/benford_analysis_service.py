from src.services.election_result_service import ElectionResultService


class BenfordAnalysisService:
    def __init__(self, election_result_service: ElectionResultService):
        self.election_result_service = election_result_service
        self.expected_distribution = [30.1, 17.6, 12.5, 9.7, 7.9, 6.7, 5.8, 5.1, 4.6]  # from Wikipedia

    def get_maximum_deviation_from_benford_distribution(self, actual_distribution):
        return max(self.calculate_deviation_from_benford_distribution(actual_distribution))

    def calculate_deviation_from_benford_distribution(self, actual_distribution):
        deviations = []
        if len(self.expected_distribution) != len(actual_distribution):
            return False
        for index in range(len(self.expected_distribution)):
            expected = self.expected_distribution[index]
            actual = actual_distribution[index]
            deviations.append(round(100 * abs(expected - actual) / expected, 2))
        return deviations

    def calculate_benford_distribution(self, election_results):
        leading_digit_occurrences = 9 * [0]
        for election_result in election_results:
            leading_digit = int(election_result.candidatevotes[0])
            leading_digit_occurrences[leading_digit - 1] += 1
        return [round(100 * int(x) / int(sum(leading_digit_occurrences)), 2) for x in leading_digit_occurrences]
