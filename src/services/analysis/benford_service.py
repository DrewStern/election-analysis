from src.services.models.election_result_service import ElectionResultService


class BenfordService:
    def __init__(self, election_result_service: ElectionResultService):
        self.election_result_service = election_result_service

        # from Wikipedia - https://en.wikipedia.org/wiki/Benford%27s_law#Generalization_to_digits_beyond_the_first
        self.first_digit_benford_distribution = [0.0, 30.1, 17.6, 12.5, 9.7, 7.9, 6.7, 5.8, 5.1, 4.6]
        self.second_digit_benford_distribution = [12.0, 11.4, 10.9, 10.4, 10.0, 9.7, 9.3, 9.0, 8.8, 8.5]
        self.third_digit_benford_distribution = [10.2, 10.1, 10.1, 10.1, 10.0, 10.0, 9.9, 9.9, 9.9, 9.8]

    def get_maximum_deviation_from_benford_distribution(self, actual_distribution):
        return max(filter(lambda x: self.is_numeric_type(x), self.calculate_deviation_from_benford_distribution(actual_distribution)))

    def calculate_deviation_from_benford_distribution(self, actual_distribution):
        deviations = []
        if len(self.first_digit_benford_distribution) != len(actual_distribution):
            return False
        for index in range(len(self.first_digit_benford_distribution)):
            expected = self.first_digit_benford_distribution[index]
            actual = actual_distribution[index]
            if expected == 0:
                deviations.append("INF")
                continue
            deviations.append(round(100 * abs(expected - actual) / expected, 2))
        return deviations

    def calculate_benford_distribution(self, election_results, digit_index=0):
        if digit_index < 0 or digit_index > 2:
            raise ValueError("digit_index may only be 0, 1, or 2")
        leading_digit_occurrences = 10 * [0]
        for election_result in election_results:
            leading_digit = int(election_result.candidatevotes[digit_index])
            leading_digit_occurrences[leading_digit] += 1
        return [round(100 * int(x) / int(sum(leading_digit_occurrences)), 2) for x in leading_digit_occurrences]

    def is_numeric_type(self, x):
        return type(x) is int or type(x) is float