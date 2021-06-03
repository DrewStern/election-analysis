from src.services.election_result_service import ElectionResultService


class BenfordAnalysisService:
    def __init__(self, election_result_service: ElectionResultService):
        self.election_result_service = election_result_service
        self.expected_distribution = [30.1, 17.6, 12.5, 9.7, 7.9, 6.7, 5.8, 5.1, 4.6]  # from Wikipedia

    def is_benford_distribution_within_tolerance(self, actual_distribution, percent_tolerance_from_expected):
        if len(self.expected_distribution) != len(actual_distribution):
            return False
        for index in range(len(self.expected_distribution)):
            expected = self.expected_distribution[index]
            actual = actual_distribution[index]
            upper_limit = expected + (expected * percent_tolerance_from_expected / 100)
            lower_limit = expected - (expected * percent_tolerance_from_expected / 100)
            if not lower_limit <= actual <= upper_limit:
                return False
        return True

    def calculate_benford_distribution(self, election_results):
        leading_digit_occurrences = 9 * [0]
        for election_result in election_results:
            leading_digit = int(election_result.candidatevotes[0])
            leading_digit_occurrences[leading_digit - 1] += 1
        return [round(100 * int(x) / int(sum(leading_digit_occurrences)), 2) for x in leading_digit_occurrences]
