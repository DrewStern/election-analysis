import unittest

from src.models.election_result import ElectionResult
from src.services.election_result_service import ElectionResultService
from src.repositories.mock_election_result_repository import MockElectionResultRepository
from src.services.prediction_analysis_service import PredictionAnalysisService


class PredictionAnalysisServiceTestCase(unittest.TestCase):
    def setUp(self):
        self.mock_prediction_rate_by_locale = dict()
        self.mock_prediction_rate_by_locale["County 1,FK"] = 1.0
        self.mock_prediction_rate_by_locale["County 2,FK"] = 0.6
        self.mock_prediction_rate_by_locale["County 3,FK"] = 0.0
        self.mock_prediction_rate_by_locale["County 4,FK"] = 1.0
        self.mock_prediction_rate_by_locale["County 5,FK"] = 0.0
        self.mock_prediction_rate_by_locale["County 6,FK"] = 0.4

        self.prediction_analysis_service = PredictionAnalysisService(ElectionResultService(MockElectionResultRepository()))

    def test_find_locales_predictive_of_winner(self):
        expected = ["County 1,FK", "County 4,FK"]
        actual = self.prediction_analysis_service.find_locales_predictive_of_winner(self.mock_prediction_rate_by_locale)
        self.assertEqual(expected, actual)

    def test_find_locales_predictive_of_loser(self):
        expected = ["County 3,FK", "County 5,FK"]
        actual = self.prediction_analysis_service.find_locales_predictive_of_loser(self.mock_prediction_rate_by_locale)
        self.assertEqual(expected, actual)

    def test_find_locales_with_prediction_rate_above(self):
        expected = ["County 1,FK", "County 2,FK", "County 4,FK"]
        actual = self.prediction_analysis_service.find_locales_with_prediction_rate_above(self.mock_prediction_rate_by_locale, 0.5)
        self.assertEqual(expected, actual)

    def test_find_locales_with_prediction_rate_below(self):
        expected = ["County 3,FK", "County 5,FK", "County 6,FK"]
        actual = self.prediction_analysis_service.find_locales_with_prediction_rate_below(self.mock_prediction_rate_by_locale, 0.5)
        self.assertEqual(expected, actual)

    # @unittest.skip("need to fix")
    # def test_get_prediction_rate_by_locale(self):
    #     expected = dict()
    #     expected["County 1,MO"] = 0.0
    #     expected["County 2,MO"] = 0.0
    #     expected["County 3,MO"] = 0.0
    #     expected["County 1,FK"] = 1.0
    #     expected["County 2,FK"] = 1.0
    #     expected["County 3,FK"] = 0.0
    #     actual = self.prediction_analysis_service.get_prediction_rate_by_locale(self.mock_election_results)
    #     self.assertEqual(expected["County 1,MO"], actual["County 1,MO"])
    #     self.assertEqual(expected["County 2,MO"], actual["County 2,MO"])
    #     self.assertEqual(expected["County 3,MO"], actual["County 3,MO"])
    #     self.assertEqual(expected["County 1,FK"], actual["County 1,FK"])
    #     self.assertEqual(expected["County 2,FK"], actual["County 2,FK"])
    #     self.assertEqual(expected["County 3,FK"], actual["County 3,FK"])

    def test_sum_correct_predictions_by_locale(self):
        pass

    def test_was_prediction_correct(self):
        election_result = ElectionResult(["1993", "MO", "Fake Candidate 1", "Fake Party 1", "120", "21000000", "County 1"])
        expected = True
        actual = self.prediction_analysis_service.was_prediction_correct(election_result)
        self.assertEqual(expected, actual)

        election_result = ElectionResult(["1993", "MO", "Fake Candidate 2", "Fake Party 2", "6900", "21000000", "County 1"])
        expected = False
        actual = self.prediction_analysis_service.was_prediction_correct(election_result)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
