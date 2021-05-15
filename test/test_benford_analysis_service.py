import unittest
from unittest import mock

from src.benford_analysis_service import BenfordAnalysisService
from src.election_result import ElectionResult
from src.election_result_repository import ElectionResultRepository


class BenfordAnalysisServiceTestCase(unittest.TestCase):
    def setUp(self):
        self.mock_election_result_data = [
            ElectionResult(["1993", "MO", "Fake Candidate 1", "Fake Party 1", "120", "21000000", "MO County 1"]),
            ElectionResult(["1993", "MO", "Fake Candidate 1", "Fake Party 1", "151", "21000000", "MO County 2"]),
            ElectionResult(["1993", "MO", "Fake Candidate 1", "Fake Party 1", "151", "21000000", "MO County 3"]),
            ElectionResult(["1993", "MO", "Fake Candidate 2", "Fake Party 2", "1900", "21000000", "MO County 1"]),
            ElectionResult(["1993", "MO", "Fake Candidate 2", "Fake Party 2", "1900", "21000000", "MO County 2"]),
            ElectionResult(["1993", "MO", "Fake Candidate 2", "Fake Party 2", "1900", "21000000", "MO County 3"]),
            ElectionResult(["1993", "MO", "Fake Candidate 3", "Fake Party 3", "1100", "21000000", "MO County 1"]),
            ElectionResult(["1993", "MO", "Fake Candidate 3", "Fake Party 3", "1100", "21000000", "MO County 2"]),
            ElectionResult(["1993", "MO", "Fake Candidate 3", "Fake Party 3", "1100", "21000000", "MO County 3"]),

            ElectionResult(["1996", "FK", "Fake Candidate 1", "Fake Party 1", "221", "22000000", "Fake County 1"]),
            ElectionResult(["1996", "FK", "Fake Candidate 1", "Fake Party 1", "22321", "22000000", "Fake County 2"]),
            ElectionResult(["1996", "FK", "Fake Candidate 1", "Fake Party 1", "221", "22000000", "Fake County 3"]),
            ElectionResult(["1996", "FK", "Fake Candidate 2", "Fake Party 2", "2901", "22000000", "Fake County 1"]),
            ElectionResult(["1996", "FK", "Fake Candidate 2", "Fake Party 2", "2901", "22000000", "Fake County 2"]),
            ElectionResult(["1996", "FK", "Fake Candidate 2", "Fake Party 2", "2901", "22000000", "Fake County 3"]),
            ElectionResult(["1996", "FK", "Fake Candidate 3", "Fake Party 3", "2101", "22000000", "Fake County 1"]),
            ElectionResult(["1996", "FK", "Fake Candidate 3", "Fake Party 3", "2101", "22000000", "Fake County 2"]),
            ElectionResult(["1996", "FK", "Fake Candidate 3", "Fake Party 3", "2101", "22000000", "Fake County 3"]),
        ]

        self.mock_leading_digit_occurrences = [1, 0, 1, 0, 1, 0, 1, 0, 1]

        self.mock_election_result_repository = ElectionResultRepository()
        self.mock_election_result_repository.get_election_results = mock.MagicMock(self.mock_election_result_data)

        self.benford_analysis_service = BenfordAnalysisService(self.mock_election_result_repository)

    def test_calculate_leading_digit_proportions_new(self):
        actual_leading_digit_proportions = self.benford_analysis_service.calculate_leading_digit_proportions_new(
            self.mock_leading_digit_occurrences)
        expected_leading_digit_proportions = [20, 0, 20, 0, 20, 0, 20, 0, 20]
        self.assertEqual(expected_leading_digit_proportions, actual_leading_digit_proportions)

    def test_sum_votes_by_leading_digit_new(self):
        expected_votes_summed_by_leading_digit = [9, 9, 0, 0, 0, 0, 0, 0, 0]
        actual_votes_summed_by_leading_digit = self.benford_analysis_service.sum_votes_by_leading_digit_new(
            self.mock_election_result_data)
        self.assertEqual(expected_votes_summed_by_leading_digit, actual_votes_summed_by_leading_digit)

    # def test_calculate_leading_digit_proportions_old(self):
    #     actual_leading_digit_proportions = self.benford_analysis_service.sum_votes_by_leading_digit_old(
    #         self.mock_election_result_data)
    #     expected_leading_digit_proportions = []
    #     self.assertEqual(expected_leading_digit_proportions, actual_leading_digit_proportions)

    def test_sum_votes_by_leading_digit_old(self):
        actual_votes_summed_by_leading_digit = self.benford_analysis_service.sum_votes_by_leading_digit_old(
            self.mock_election_result_data)

        expected_ones = 3
        actual_ones = actual_votes_summed_by_leading_digit["1993"]["Fake Candidate 1"][0]
        self.assertEqual(expected_ones, actual_ones)

        expected_fours = 0
        actual_fours = actual_votes_summed_by_leading_digit["1993"]["Fake Candidate 1"][3]
        self.assertEqual(expected_fours, actual_fours)

        expected_sixes = 0
        actual_sixes = actual_votes_summed_by_leading_digit["1993"]["Fake Candidate 2"][5]
        self.assertEqual(expected_sixes, actual_sixes)


if __name__ == '__main__':
    unittest.main()
