import unittest
from unittest import mock

from src.election_result import ElectionResult
from src.election_result_repository import ElectionResultRepository
from src.predictiveness_analysis_service import PredictivenessAnalysisService


class PredictivenessAnalysisServiceTestCase(unittest.TestCase):
    def setUp(self):
        self.mock_election_result_data = [
            ElectionResult(["1993", "MO", "Fake Candidate 1", "Fake Party 1", "120", "21000000", "County 1"]),
            ElectionResult(["1993", "MO", "Fake Candidate 1", "Fake Party 1", "451", "21000000", "County 2"]),
            ElectionResult(["1993", "MO", "Fake Candidate 1", "Fake Party 1", "451", "21000000", "County 3"]),
            ElectionResult(["1993", "MO", "Fake Candidate 2", "Fake Party 2", "6900", "21000000", "County 1"]),
            ElectionResult(["1993", "MO", "Fake Candidate 2", "Fake Party 2", "6900", "21000000", "County 2"]),
            ElectionResult(["1993", "MO", "Fake Candidate 2", "Fake Party 2", "6900", "21000000", "County 3"]),

            ElectionResult(["1997", "FK", "Fake Candidate 1", "Fake Party 1", "121", "22000000", "County 1"]),
            ElectionResult(["1997", "FK", "Fake Candidate 2", "Fake Party 1", "12321", "22000000", "County 2"]),
            ElectionResult(["1997", "FK", "Fake Candidate 1", "Fake Party 1", "421", "22000000", "County 3"]),
            ElectionResult(["1997", "FK", "Fake Candidate 2", "Fake Party 2", "1901", "22000000", "County 1"]),
            ElectionResult(["1997", "FK", "Fake Candidate 1", "Fake Party 2", "9901", "22000000", "County 2"]),
            ElectionResult(["1997", "FK", "Fake Candidate 2", "Fake Party 2", "6901", "22000000", "County 3"]),

            ElectionResult(["2001", "MO", "Fake Candidate 1", "Fake Party 1", "120", "21000000", "County 1"]),
            ElectionResult(["2001", "MO", "Fake Candidate 1", "Fake Party 1", "451", "21000000", "County 2"]),
            ElectionResult(["2001", "MO", "Fake Candidate 2", "Fake Party 1", "451", "21000000", "County 3"]),
            ElectionResult(["2001", "MO", "Fake Candidate 2", "Fake Party 2", "6900", "21000000", "County 1"]),
            ElectionResult(["2001", "MO", "Fake Candidate 1", "Fake Party 2", "6900", "21000000", "County 2"]),
            ElectionResult(["2001", "MO", "Fake Candidate 2", "Fake Party 2", "6900", "21000000", "County 3"]),

            ElectionResult(["2005", "FK", "Fake Candidate 1", "Fake Party 1", "121", "22000000", "County 1"]),
            ElectionResult(["2005", "FK", "Fake Candidate 2", "Fake Party 1", "12321", "22000000", "County 2"]),
            ElectionResult(["2005", "FK", "Fake Candidate 2", "Fake Party 1", "421", "22000000", "County 3"]),
            ElectionResult(["2005", "FK", "Fake Candidate 1", "Fake Party 2", "1901", "22000000", "County 1"]),
            ElectionResult(["2005", "FK", "Fake Candidate 1", "Fake Party 2", "9901", "22000000", "County 2"]),
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

        self.mock_election_result_repository = ElectionResultRepository()
        self.mock_election_result_repository.get_election_results = mock.MagicMock(self.mock_election_result_data)
        self.mock_election_result_repository.get_nationally_winning_candidates_by_year = mock.MagicMock(self.mock_nationally_winning_candidates_by_year)
        self.mock_election_result_repository.get_nationally_losing_candidates_by_year = mock.MagicMock(self.mock_nationally_losing_candidates_by_year)

        self.mock_election_predictiveness_analysis_service = PredictivenessAnalysisService(
            self.mock_election_result_repository)

    def test_get_locale_election_winner_by_year(self):
        expected_county_election_winner_by_year = "Fake Candidate 2"
        actual_county_election_winner_by_year = self.mock_election_predictiveness_analysis_service.get_locale_election_winner_by_year(
            self.mock_election_result_data, "1993", "County 3", "MO")
        self.assertTrue(expected_county_election_winner_by_year, actual_county_election_winner_by_year)

    def test_get_prediction_rate_by_county_new(self):
        expected_prediction_rate_by_county = dict()
        expected_prediction_rate_by_county["County 1"] = 1.0
        # expected_prediction_rate_by_county["County 2"] = 1.0
        expected_prediction_rate_by_county["County 3"] = 0.0
        actual_prediction_rate_by_county = self.mock_election_predictiveness_analysis_service.get_prediction_rate_by_county_new(self.mock_election_result_data)
        self.assertTrue(expected_prediction_rate_by_county, actual_prediction_rate_by_county)

if __name__ == '__main__':
    unittest.main()
