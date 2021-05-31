import unittest

from src.services.election_result_service import ElectionResultService
from src.repositories.mock_election_result_repository import MockElectionResultRepository
from src.services.prediction_analysis_service import PredictionAnalysisService


class PredictionAnalysisServiceTestCase(unittest.TestCase):
    def setUp(self):
        self.mock_prediction_rate_by_locale = dict()
        self.mock_prediction_rate_by_locale["County 1,FK"] = 1.0
        self.mock_prediction_rate_by_locale["County 2,FK"] = 0.6
        self.mock_prediction_rate_by_locale["County 3,FK"] = 0.0
        self.mock_prediction_rate_by_locale["County 4,FK"] = 0.8
        self.mock_prediction_rate_by_locale["County 5,FK"] = 0.2
        self.mock_prediction_rate_by_locale["County 6,FK"] = 0.4

        self.mock_election_result_repository = MockElectionResultRepository()
        self.prediction_analysis_service = PredictionAnalysisService(ElectionResultService(self.mock_election_result_repository))

    def test_find_locales_with_prediction_rate_above(self):
        expected = ["County 1,FK", "County 2,FK", "County 3,FK", "County 4,FK", "County 5,FK", "County 6,FK"]
        actual = self.prediction_analysis_service.find_locales_with_prediction_rate_above(self.mock_prediction_rate_by_locale, 0.0)
        self.assertEqual(expected, actual)

        expected = ["County 1,FK", "County 2,FK", "County 4,FK"]
        actual = self.prediction_analysis_service.find_locales_with_prediction_rate_above(self.mock_prediction_rate_by_locale, 0.5)
        self.assertEqual(expected, actual)

        expected = ["County 1,FK"]
        actual = self.prediction_analysis_service.find_locales_with_prediction_rate_above(self.mock_prediction_rate_by_locale, 1.0)
        self.assertEqual(expected, actual)

    def test_find_locales_with_prediction_rate_below(self):
        expected = ["County 3,FK"]
        actual = self.prediction_analysis_service.find_locales_with_prediction_rate_below(self.mock_prediction_rate_by_locale, 0.0)
        self.assertEqual(expected, actual)

        expected = ["County 3,FK", "County 5,FK", "County 6,FK"]
        actual = self.prediction_analysis_service.find_locales_with_prediction_rate_below(self.mock_prediction_rate_by_locale, 0.5)
        self.assertEqual(expected, actual)

        expected = ["County 1,FK", "County 2,FK", "County 3,FK", "County 4,FK", "County 5,FK", "County 6,FK"]
        actual = self.prediction_analysis_service.find_locales_with_prediction_rate_below(self.mock_prediction_rate_by_locale, 1.0)
        self.assertEqual(expected, actual)

    def test_get_locale_prediction_ranking(self):
        pass

    def test_get_prediction_rate_by_locale(self):
        expected = dict()
        expected["County 1,MO"] = 0.0
        expected["County 2,MO"] = 0.0
        expected["County 3,MO"] = 0.0
        # TODO: this should actually be 1.0 but requires adding test data for County 1,FK results in 1993 and 2001
        expected["County 1,FK"] = 0.5
        expected["County 2,FK"] = 0.0
        expected["County 3,FK"] = 0.0
        actual = self.prediction_analysis_service.get_prediction_rate_by_locale(self.mock_election_result_repository.get_election_results())
        self.assertEqual(expected, actual)

    def test_sum_correct_predictions_by_locale(self):
        expected = dict()
        expected["County 1,MO"] = 0
        expected["County 2,MO"] = 0
        expected["County 3,MO"] = 0
        expected["County 1,FK"] = 2
        expected["County 2,FK"] = 0
        expected["County 3,FK"] = 0
        actual = self.prediction_analysis_service.sum_correct_predictions_by_locale(self.mock_election_result_repository.get_election_results())
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
