import unittest

from src.main import read_presidential_votes_county_data
from src.repositories.election_result_repository import ElectionResultRepository
from src.services.election_result_service import ElectionResultService
from src.services.benford_analysis_service import BenfordAnalysisService


class MainIntegrationTestCases(unittest.TestCase):
    def setUp(self) -> None:
        self.election_result_repository = ElectionResultRepository(read_presidential_votes_county_data())
        self.election_result_service = ElectionResultService(self.election_result_repository)
        self.benford_analysis_service = BenfordAnalysisService(self.election_result_service)

    # Note: the expected values here are basically just copy/paste of the service output.
    # I did not go through the data set to manually calculate and double check these values.
    # The tolerances supplied to is_within_tolerance are the smallest integer such that the test passes.
    # Decrementing any of these parameters will cause the test to fail.
    def test_calculate_benford_distribution(self):
        expected = [28.79, 17.83, 13.07, 10.37, 8.27, 6.7, 5.6, 4.98, 4.38]
        actual = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results())
        self.assertEqual(expected, actual)

        expected = [28.62, 19.32, 12.66, 11.01, 8.15, 6.35, 4.89, 5.46, 3.55]
        actual = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(candidate_filter="Al Gore"))
        self.assertEqual(expected, actual)

        given_distribution = actual
        is_within_tolerance = self.benford_analysis_service.is_benford_distribution_within_tolerance(given_distribution, 23)
        self.assertTrue(is_within_tolerance)

        expected = [28.48, 17.36, 13.72, 10.18, 8.25, 6.96, 5.77, 4.93, 4.35]
        actual = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(candidate_filter="George W. Bush"))
        self.assertEqual(expected, actual)

        given_distribution = actual
        is_within_tolerance = self.benford_analysis_service.is_benford_distribution_within_tolerance(given_distribution, 10)
        self.assertTrue(is_within_tolerance)

        expected = [28.38, 18.83, 12.71, 10.81, 8.85, 6.66, 4.85, 4.63, 4.28]
        actual = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(candidate_filter="John Kerry"))
        self.assertEqual(expected, actual)

        given_distribution = actual
        is_within_tolerance = self.benford_analysis_service.is_benford_distribution_within_tolerance(given_distribution, 17)
        self.assertTrue(is_within_tolerance)

        expected = [28.64, 18.87, 13.2, 10.19, 7.77, 6.45, 5.55, 4.5, 4.83]
        actual = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(candidate_filter="Barack Obama"))
        self.assertEqual(expected, actual)

        given_distribution = actual
        is_within_tolerance = self.benford_analysis_service.is_benford_distribution_within_tolerance(given_distribution, 12)
        self.assertTrue(is_within_tolerance)

        expected = [28.47, 16.84, 12.78, 10.59, 8.85, 6.82, 5.74, 5.36, 4.57]
        actual = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(candidate_filter="John McCain"))
        self.assertEqual(expected, actual)

        given_distribution = actual
        is_within_tolerance = self.benford_analysis_service.is_benford_distribution_within_tolerance(given_distribution, 13)
        self.assertTrue(is_within_tolerance)

        expected = [28.83, 16.48, 12.77, 10.74, 8.78, 7.13, 5.61, 5.45, 4.21]
        actual = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(candidate_filter="Mitt Romney"))
        self.assertEqual(expected, actual)

        given_distribution = actual
        is_within_tolerance = self.benford_analysis_service.is_benford_distribution_within_tolerance(given_distribution, 12)
        self.assertTrue(is_within_tolerance)

        expected = [29.91, 18.31, 13.62, 9.57, 6.91, 6.34, 6.4, 4.47, 4.47]
        actual = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(candidate_filter="Hillary Clinton"))
        self.assertEqual(expected, actual)

        given_distribution = actual
        is_within_tolerance = self.benford_analysis_service.is_benford_distribution_within_tolerance(given_distribution, 13)
        self.assertTrue(is_within_tolerance)

        expected = [29.44, 16.03, 12.36, 10.23, 9.19, 6.88, 5.93, 5.54, 4.4]
        actual = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(candidate_filter="Donald Trump"))
        self.assertEqual(expected, actual)

        given_distribution = actual
        is_within_tolerance = self.benford_analysis_service.is_benford_distribution_within_tolerance(given_distribution, 17)
        self.assertTrue(is_within_tolerance)


if __name__ == '__main__':
    unittest.main()
