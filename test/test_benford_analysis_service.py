import unittest
from unittest import mock

from src.benford_analysis_service import BenfordAnalysisService
from src.election_result import ElectionResult


class BenfordAnalysisServiceTestCase(unittest.TestCase):
    def setUp(self):
        self.mock_election_result_data = [
            ElectionResult(["1993", "MO", "Fake Candidate 1", "Fake Party 1", "120", "21000000", "MO County 1"]),
            ElectionResult(["1993", "MO", "Fake Candidate 1", "Fake Party 1", "151", "21000000", "MO County 2"]),
            ElectionResult(["1993", "MO", "Fake Candidate 1", "Fake Party 1", "151", "21000000", "MO County 3"]),
            ElectionResult(["1993", "MO", "Fake Candidate 2", "Fake Party 2", "1900", "21000000", "MO County 1"]),
            ElectionResult(["1993", "MO", "Fake Candidate 2", "Fake Party 2", "1900", "21000000", "MO County 2"]),
            ElectionResult(["1993", "MO", "Fake Candidate 2", "Fake Party 2", "1900", "21000000", "MO County 3"]),
            ElectionResult(["1993", "MO", "Fake Candidate 3", "Fake Party 3", "9100", "21000000", "MO County 1"]),
            ElectionResult(["1993", "MO", "Fake Candidate 3", "Fake Party 3", "9100", "21000000", "MO County 2"]),
            ElectionResult(["1993", "MO", "Fake Candidate 3", "Fake Party 3", "9100", "21000000", "MO County 3"]),

            ElectionResult(["1996", "FK", "Fake Candidate 1", "Fake Party 1", "921", "22000000", "Fake County 1"]),
            ElectionResult(["1996", "FK", "Fake Candidate 1", "Fake Party 1", "92321", "22000000", "Fake County 2"]),
            ElectionResult(["1996", "FK", "Fake Candidate 1", "Fake Party 1", "921", "22000000", "Fake County 3"]),
            ElectionResult(["1996", "FK", "Fake Candidate 2", "Fake Party 2", "2901", "22000000", "Fake County 1"]),
            ElectionResult(["1996", "FK", "Fake Candidate 2", "Fake Party 2", "2901", "22000000", "Fake County 2"]),
            ElectionResult(["1996", "FK", "Fake Candidate 2", "Fake Party 2", "2901", "22000000", "Fake County 3"]),
            ElectionResult(["1996", "FK", "Fake Candidate 3", "Fake Party 3", "2101", "22000000", "Fake County 1"]),
            ElectionResult(["1996", "FK", "Fake Candidate 3", "Fake Party 3", "2101", "22000000", "Fake County 2"]),
            ElectionResult(["1996", "FK", "Fake Candidate 3", "Fake Party 3", "2101", "22000000", "Fake County 3"]),
        ]

        self.benford_analysis_service = BenfordAnalysisService()

    def test_calculate_benford_distribution(self):
        actual_benford_distribution = self.benford_analysis_service.calculate_benford_distribution(
            self.mock_election_result_data)
        expected_benford_distribution = [33.33, 33.33, 0, 0, 0, 0, 0, 0, 33.33]
        self.assertEqual(expected_benford_distribution, actual_benford_distribution)


if __name__ == '__main__':
    unittest.main()
