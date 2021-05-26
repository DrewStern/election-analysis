import unittest
from unittest import mock
from unittest.mock import create_autospec

from src.election_result import ElectionResult
from src.election_result_repository import ElectionResultRepository
from src.predictiveness_analysis_service import PredictivenessAnalysisService


class PredictivenessAnalysisServiceTestCase(unittest.TestCase):
    def setUp(self):
        self.mock_election_results = [
            ElectionResult(["1993", "MO", "Fake Candidate 1", "Fake Party 1", "120", "21000000", "County 1"]),
            ElectionResult(["1993", "MO", "Fake Candidate 2", "Fake Party 2", "6900", "21000000", "County 1"]),

            ElectionResult(["1993", "MO", "Fake Candidate 1", "Fake Party 1", "451", "21000000", "County 2"]),
            ElectionResult(["1993", "MO", "Fake Candidate 2", "Fake Party 2", "6900", "21000000", "County 2"]),

            ElectionResult(["1993", "MO", "Fake Candidate 1", "Fake Party 1", "451", "21000000", "County 3"]),
            ElectionResult(["1993", "MO", "Fake Candidate 2", "Fake Party 2", "6900", "21000000", "County 3"]),

            ElectionResult(["1997", "FK", "Fake Candidate 1", "Fake Party 1", "121111", "22000000", "County 1"]),
            ElectionResult(["1997", "FK", "Fake Candidate 2", "Fake Party 2", "1901", "22000000", "County 1"]),

            ElectionResult(["1997", "FK", "Fake Candidate 1", "Fake Party 1", "9901", "22000000", "County 2"]),
            ElectionResult(["1997", "FK", "Fake Candidate 2", "Fake Party 2", "12321", "22000000", "County 2"]),

            ElectionResult(["1997", "FK", "Fake Candidate 1", "Fake Party 1", "421", "22000000", "County 3"]),
            ElectionResult(["1997", "FK", "Fake Candidate 2", "Fake Party 2", "6901", "22000000", "County 3"]),

            ElectionResult(["2001", "MO", "Fake Candidate 1", "Fake Party 1", "120", "21000000", "County 1"]),
            ElectionResult(["2001", "MO", "Fake Candidate 2", "Fake Party 2", "6900", "21000000", "County 1"]),

            ElectionResult(["2001", "MO", "Fake Candidate 1", "Fake Party 1", "451", "21000000", "County 2"]),
            ElectionResult(["2001", "MO", "Fake Candidate 2", "Fake Party 2", "6900", "21000000", "County 2"]),

            ElectionResult(["2001", "MO", "Fake Candidate 1", "Fake Party 1", "451", "21000000", "County 3"]),
            ElectionResult(["2001", "MO", "Fake Candidate 2", "Fake Party 2", "6900", "21000000", "County 3"]),

            ElectionResult(["2005", "FK", "Fake Candidate 1", "Fake Party 1", "121111", "22000000", "County 1"]),
            ElectionResult(["2005", "FK", "Fake Candidate 2", "Fake Party 2", "1901", "22000000", "County 1"]),

            ElectionResult(["2005", "FK", "Fake Candidate 1", "Fake Party 1", "9901", "22000000", "County 2"]),
            ElectionResult(["2005", "FK", "Fake Candidate 2", "Fake Party 2", "12321", "22000000", "County 2"]),

            ElectionResult(["2005", "FK", "Fake Candidate 1", "Fake Party 1", "421", "22000000", "County 3"]),
            ElectionResult(["2005", "FK", "Fake Candidate 2", "Fake Party 2", "6901", "22000000", "County 3"]),
        ]

        self.mock_nationally_winning_candidates_by_year = dict()
        self.mock_nationally_winning_candidates_by_year["1993"] = "Fake Candidate 1"
        self.mock_nationally_winning_candidates_by_year["1997"] = "Fake Candidate 1"
        self.mock_nationally_winning_candidates_by_year["2001"] = "Fake Candidate 1"
        self.mock_nationally_winning_candidates_by_year["2005"] = "Fake Candidate 1"

        self.mock_nationally_losing_candidates_by_year = dict()
        self.mock_nationally_losing_candidates_by_year["1993"] = "Fake Candidate 2"
        self.mock_nationally_losing_candidates_by_year["1997"] = "Fake Candidate 2"
        self.mock_nationally_losing_candidates_by_year["2001"] = "Fake Candidate 2"
        self.mock_nationally_losing_candidates_by_year["2005"] = "Fake Candidate 2"

        self.mock_prediction_rate_by_county = dict()
        self.mock_prediction_rate_by_county["County 1,FK"] = 1.0
        self.mock_prediction_rate_by_county["County 2,FK"] = 0.5
        self.mock_prediction_rate_by_county["County 3,FK"] = 0.0
        self.mock_prediction_rate_by_county["County 4,FK"] = 1.0
        self.mock_prediction_rate_by_county["County 5,FK"] = 0.0

        self.mock_election_result_repository = ElectionResultRepository()
        self.mock_election_result_repository.get_election_results = mock.MagicMock(self.mock_election_results)
        self.mock_election_result_repository.get_nationally_winning_candidates_by_year = mock.MagicMock(self.mock_nationally_winning_candidates_by_year)
        self.mock_election_result_repository.get_nationally_losing_candidates_by_year = mock.MagicMock(self.mock_nationally_losing_candidates_by_year)

        self.predictiveness_analysis_service = PredictivenessAnalysisService(self.mock_election_result_repository)

    def test_get_election_winner(self):
        expected = "Fake Candidate 2"
        actual = self.predictiveness_analysis_service.get_election_winner(self.mock_election_results, "1993", "County 3", "MO")
        self.assertEqual(expected, actual)

        expected = "Fake Candidate 1"
        actual = self.predictiveness_analysis_service.get_election_winner(self.mock_election_results, "1997", "County 1", "FK")
        self.assertEqual(expected, actual)

        expected = "Fake Candidate 2"
        actual = self.predictiveness_analysis_service.get_election_winner(self.mock_election_results, "2001", "County 2", "MO")
        self.assertEqual(expected, actual)

        expected = "Fake Candidate 2"
        actual = self.predictiveness_analysis_service.get_election_winner(self.mock_election_results, "2005", "County 3", "FK")
        self.assertEqual(expected, actual)

    def test_get_prediction_rate_by_county(self):
        expected = dict()
        expected["County 1,MO"] = 0.0
        expected["County 2,MO"] = 0.0
        expected["County 3,MO"] = 0.0
        expected["County 1,FK"] = 1.0
        expected["County 2,FK"] = 1.0
        expected["County 3,FK"] = 0.0
        actual = self.predictiveness_analysis_service.get_prediction_rate_by_county(self.mock_election_results)
        self.assertEqual(expected["County 1,MO"], actual["County 1,MO"])
        self.assertEqual(expected["County 2,MO"], actual["County 2,MO"])
        self.assertEqual(expected["County 3,MO"], actual["County 3,MO"])
        # self.assertEqual(expected["County 1,FK"], actual["County 1,FK"])
        # self.assertEqual(expected["County 2,FK"], actual["County 2,FK"])
        self.assertEqual(expected["County 3,FK"], actual["County 3,FK"])

    def test_find_counties_predictive_of_winner(self):
        expected = ["County 1,FK", "County 4,FK"]
        actual = self.predictiveness_analysis_service.find_counties_predictive_of_winner(self.mock_prediction_rate_by_county)
        self.assertEqual(expected, actual)

    def test_find_counties_predictive_of_loser(self):
        expected = ["County 3,FK", "County 5,FK"]
        actual = self.predictiveness_analysis_service.find_counties_predictive_of_loser(self.mock_prediction_rate_by_county)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
