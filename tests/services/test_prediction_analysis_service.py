import unittest

from src.repositories.mock_election_result_repository import MockElectionResultRepository
from src.services.election_result_service import ElectionResultService
from src.services.locality_result_service import LocalityResultService
from src.services.analysis.prediction_analysis_service import PredictionAnalysisService


class PredictionAnalysisServiceTestCases(unittest.TestCase):
    def setUp(self):
        self.mock_prediction_rate_by_locale = dict()
        self.mock_prediction_rate_by_locale["County 1,FK"] = 1.0
        self.mock_prediction_rate_by_locale["County 2,FK"] = 0.6
        self.mock_prediction_rate_by_locale["County 3,FK"] = 0.0
        self.mock_prediction_rate_by_locale["County 4,FK"] = 0.8
        self.mock_prediction_rate_by_locale["County 5,FK"] = 0.2
        self.mock_prediction_rate_by_locale["County 6,FK"] = 0.4

        self.mock_election_result_repository = MockElectionResultRepository()
        self.election_result_service = ElectionResultService(self.mock_election_result_repository)
        self.locality_result_service = LocalityResultService(self.election_result_service)
        self.prediction_analysis_service = PredictionAnalysisService(self.locality_result_service)

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
        expected = ["County 1,FK", "County 1,MO", "County 2,MO", "County 3,FK", "County 2,FK", "County 3,MO"]
        actual = self.prediction_analysis_service.get_locale_prediction_ranking()
        self.assertEqual(expected, actual)

    def test_get_prediction_rate_by_locale(self):
        expected = dict()
        # TODO: these values might be half of what you're expecting
        # e.g., County1,FK has 1.0 prediction rate in the elections it's been in
        # but it's only been in 0.5 of the elections (participation rate)
        # so expected prediction rate = 0.5; likewise for all others
        # this can be "fixed" by putting MO and FK for all election years
        expected["County 1,MO"] = 0.25
        expected["County 2,MO"] = 0.25
        expected["County 3,MO"] = 0.0
        expected["County 1,FK"] = 0.5
        expected["County 2,FK"] = 0.0
        expected["County 3,FK"] = 0.25
        actual = self.prediction_analysis_service.get_prediction_rate_by_locale()
        self.assertEqual(expected, actual)

    def test_sum_correct_predictions_by_locale(self):
        expected = dict()
        expected["County 1,MO"] = 1
        expected["County 2,MO"] = 1
        expected["County 3,MO"] = 0
        expected["County 1,FK"] = 2
        expected["County 2,FK"] = 0
        expected["County 3,FK"] = 1
        actual = self.prediction_analysis_service.sum_correct_predictions_by_locale()
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
