import datetime
import os
import unittest
from pathlib import Path

from src.repositories.election_result_repository import ElectionResultRepository
from src.services.election_result_service import ElectionResultService
from src.services.benford_analysis_service import BenfordAnalysisService


# The expected values here are basically just copy/paste of the service output.
# I did not go through the data set to manually calculate and double check these values.
# However, the unit tests WERE manually calculated and verified. Which lends weight to the validity of these results.
# The tolerances supplied to is_within_tolerance throughout are the smallest integer such that the test passes.
# Decrementing any of these parameters will cause the test to fail.
class MitIntegrationTestCases(unittest.TestCase):
    def setUp(self) -> None:
        data_path = self.read_presidential_votes_county_data()
        self.election_result_repository = ElectionResultRepository(data_path)
        self.election_result_service = ElectionResultService(self.election_result_repository)
        self.benford_analysis_service = BenfordAnalysisService(self.election_result_service)

    def test_calculate_benford_distribution(self):
        expected = [28.85, 17.68, 12.74, 10.17, 8.07, 6.57, 5.53, 4.98, 5.42]
        actual = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results())
        self.assertEqual(expected, actual)
        expected_deviations = [4.15, 0.45, 1.92, 4.85, 2.15, 1.94, 4.66, 2.35, 17.83]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual)
        self.assertEqual(expected_deviations, actual_deviations)
        is_within_tolerance = self.benford_analysis_service.is_benford_distribution_within_tolerance(actual, 18)
        self.assertTrue(is_within_tolerance)

    def test_calculate_benford_distribution_by_candidate(self):
        expected = [28.62, 19.32, 12.66, 11.01, 8.15, 6.35, 4.89, 5.46, 3.55]
        actual = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(candidate_filter="Al Gore"))
        self.assertEqual(expected, actual)
        expected_deviations = [4.92, 9.77, 1.28, 13.51, 3.16, 5.22, 15.69, 7.06, 22.83]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual)
        self.assertEqual(expected_deviations, actual_deviations)
        is_within_tolerance = self.benford_analysis_service.is_benford_distribution_within_tolerance(actual, 23)
        self.assertTrue(is_within_tolerance)

        expected = [28.48, 17.36, 13.72, 10.18, 8.25, 6.96, 5.77, 4.93, 4.35]
        actual = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(candidate_filter="George W. Bush"))
        self.assertEqual(expected, actual)
        expected_deviations = [5.38, 1.36, 9.76, 4.95, 4.43, 3.88, 0.52, 3.33, 5.43]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual)
        self.assertEqual(expected_deviations, actual_deviations)
        is_within_tolerance = self.benford_analysis_service.is_benford_distribution_within_tolerance(actual, 10)
        self.assertTrue(is_within_tolerance)

        expected = [28.38, 18.83, 12.71, 10.81, 8.85, 6.66, 4.85, 4.63, 4.28]
        actual = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(candidate_filter="John Kerry"))
        self.assertEqual(expected, actual)
        expected_deviations = [5.71, 6.99, 1.68, 11.44, 12.03, 0.6, 16.38, 9.22, 6.96]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual)
        self.assertEqual(expected_deviations, actual_deviations)
        is_within_tolerance = self.benford_analysis_service.is_benford_distribution_within_tolerance(actual, 17)
        self.assertTrue(is_within_tolerance)

        expected = [28.64, 18.87, 13.2, 10.19, 7.77, 6.45, 5.55, 4.5, 4.83]
        actual = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(candidate_filter="Barack Obama"))
        self.assertEqual(expected, actual)
        expected_deviations = [4.85, 7.22, 5.6, 5.05, 1.65, 3.73, 4.31, 11.76, 5.0]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual)
        self.assertEqual(expected_deviations, actual_deviations)
        is_within_tolerance = self.benford_analysis_service.is_benford_distribution_within_tolerance(actual, 12)
        self.assertTrue(is_within_tolerance)

        expected = [28.47, 16.84, 12.78, 10.59, 8.85, 6.82, 5.74, 5.36, 4.57]
        actual = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(candidate_filter="John McCain"))
        self.assertEqual(expected, actual)
        expected_deviations = [5.42, 4.32, 2.24, 9.18, 12.03, 1.79, 1.03, 5.1, 0.65]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual)
        self.assertEqual(expected_deviations, actual_deviations)
        is_within_tolerance = self.benford_analysis_service.is_benford_distribution_within_tolerance(actual, 13)
        self.assertTrue(is_within_tolerance)

        expected = [28.83, 16.48, 12.77, 10.74, 8.78, 7.13, 5.61, 5.45, 4.21]
        actual = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(candidate_filter="Mitt Romney"))
        self.assertEqual(expected, actual)
        expected_deviations = [4.22, 6.36, 2.16, 10.72, 11.14, 6.42, 3.28, 6.86, 8.48]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual)
        self.assertEqual(expected_deviations, actual_deviations)
        is_within_tolerance = self.benford_analysis_service.is_benford_distribution_within_tolerance(actual, 12)
        self.assertTrue(is_within_tolerance)

        expected = [29.91, 18.31, 13.62, 9.57, 6.91, 6.34, 6.4, 4.47, 4.47]
        actual = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(candidate_filter="Hillary Clinton"))
        self.assertEqual(expected, actual)
        expected_deviations = [0.63, 4.03, 8.96, 1.34, 12.53, 5.37, 10.34, 12.35, 2.83]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual)
        self.assertEqual(expected_deviations, actual_deviations)
        is_within_tolerance = self.benford_analysis_service.is_benford_distribution_within_tolerance(actual, 13)
        self.assertTrue(is_within_tolerance)

        # Note that this references Trump's 2016 results
        expected = [29.44, 16.03, 12.36, 10.23, 9.19, 6.88, 5.93, 5.54, 4.4]
        actual = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(candidate_filter="Donald Trump"))
        self.assertEqual(expected, actual)
        expected_deviations = [2.19, 8.92, 1.12, 5.46, 16.33, 2.69, 2.24, 8.63, 4.35]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual)
        self.assertEqual(expected_deviations, actual_deviations)
        is_within_tolerance = self.benford_analysis_service.is_benford_distribution_within_tolerance(actual, 17)
        self.assertTrue(is_within_tolerance)

        # Note that this references Trump's 2020 results
        expected = [29.49, 17.31, 11.2, 9.11, 7.7, 6.23, 5.41, 5.02, 8.52]
        actual = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(candidate_filter="Donald J Trump"))
        self.assertEqual(expected, actual)
        expected_deviations = [2.03, 1.65, 10.4, 6.08, 2.53, 7.01, 6.72, 1.57, 85.22]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual)
        self.assertEqual(expected_deviations, actual_deviations)
        is_within_tolerance = self.benford_analysis_service.is_benford_distribution_within_tolerance(actual, 86)
        self.assertTrue(is_within_tolerance)

        expected = [28.55, 17.11, 12.25, 9.99, 7.17, 6.07, 5.15, 4.98, 8.72]
        actual = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(candidate_filter="Joseph R Biden Jr"))
        self.assertEqual(expected, actual)
        expected_deviations = [5.15, 2.78, 2.0, 2.99, 9.24, 9.4, 11.21, 2.35, 89.57]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual)
        self.assertEqual(expected_deviations, actual_deviations)
        is_within_tolerance = self.benford_analysis_service.is_benford_distribution_within_tolerance(actual, 90)
        self.assertTrue(is_within_tolerance)

    def test_calculate_benford_distribution_by_party(self):
        expected = [28.77, 18.42, 12.88, 10.27, 7.71, 6.36, 5.37, 4.78, 5.45]
        actual = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(party_filter="Democrat"))
        self.assertEqual(expected, actual)
        expected_deviations = [4.42, 4.66, 3.04, 5.88, 2.41, 5.07, 7.41, 6.27, 18.48]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual)
        self.assertEqual(expected_deviations, actual_deviations)
        is_within_tolerance = self.benford_analysis_service.is_benford_distribution_within_tolerance(actual, 19)
        self.assertTrue(is_within_tolerance)

        expected = [28.92, 16.94, 12.61, 10.07, 8.43, 6.77, 5.68, 5.19, 5.39]
        actual = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(party_filter="Republican"))
        self.assertEqual(expected, actual)
        expected_deviations = [3.92, 3.75, 0.88, 3.81, 6.71, 1.04, 2.07, 1.76, 17.17]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual)
        self.assertEqual(expected_deviations, actual_deviations)
        is_within_tolerance = self.benford_analysis_service.is_benford_distribution_within_tolerance(actual, 18)
        self.assertTrue(is_within_tolerance)

    def test_calculate_benford_distribution_by_state(self):
        expected = [26.72, 18.82, 13.36, 9.48, 9.2, 7.04, 5.6, 4.89, 4.89]
        actual = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(state_filter="CA"))
        self.assertEqual(expected, actual)
        expected_deviations = [11.23, 6.93, 6.88, 2.27, 16.46, 5.07, 3.45, 4.12, 6.3]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual)
        self.assertEqual(expected_deviations, actual_deviations)
        is_within_tolerance = self.benford_analysis_service.is_benford_distribution_within_tolerance(actual, 17)
        self.assertTrue(is_within_tolerance)

        expected = [26.37, 19.15, 12.06, 10.95, 8.58, 8.46, 5.47, 5.35, 3.61]
        actual = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(state_filter="FL"))
        self.assertEqual(expected, actual)
        expected_deviations = [12.39, 8.81, 3.52, 12.89, 8.61, 26.27, 5.69, 4.9, 21.52]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual)
        self.assertEqual(expected_deviations, actual_deviations)
        is_within_tolerance = self.benford_analysis_service.is_benford_distribution_within_tolerance(actual, 27)
        self.assertTrue(is_within_tolerance)

        expected = [29.17, 15.28, 13.15, 11.11, 9.56, 7.03, 4.33, 4.9, 5.47]
        actual = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(state_filter="IL"))
        self.assertEqual(expected, actual)
        expected_deviations = [3.09, 13.18, 5.2, 14.54, 21.01, 4.93, 25.34, 3.92, 18.91]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual)
        self.assertEqual(expected_deviations, actual_deviations)
        is_within_tolerance = self.benford_analysis_service.is_benford_distribution_within_tolerance(actual, 26)
        self.assertTrue(is_within_tolerance)

        expected = [28.2, 18.35, 14.24, 11.22, 8.85, 6.04, 5.4, 3.31, 4.39]
        actual = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(state_filter="MO"))
        self.assertEqual(expected, actual)
        expected_deviations = [6.31, 4.26, 13.92, 15.67, 12.03, 9.85, 6.9, 35.1, 4.57]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual)
        self.assertEqual(expected_deviations, actual_deviations)
        is_within_tolerance = self.benford_analysis_service.is_benford_distribution_within_tolerance(actual, 36)
        self.assertTrue(is_within_tolerance)

        expected = [37.63, 14.38, 9.27, 8.2, 7.12, 6.45, 4.7, 5.65, 6.59]
        actual = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(state_filter="NY"))
        self.assertEqual(expected, actual)
        expected_deviations = [25.02, 18.3, 25.84, 15.46, 9.87, 3.73, 18.97, 10.78, 43.26]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual)
        self.assertEqual(expected_deviations, actual_deviations)
        is_within_tolerance = self.benford_analysis_service.is_benford_distribution_within_tolerance(actual, 44)
        self.assertTrue(is_within_tolerance)

        expected = [33.62, 12.97, 12.12, 9.94, 7.48, 7.95, 6.63, 4.92, 4.36]
        actual = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(state_filter="OH"))
        self.assertEqual(expected, actual)
        expected_deviations = [11.69, 26.31, 3.04, 2.47, 5.32, 18.66, 14.31, 3.53, 5.22]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual)
        self.assertEqual(expected_deviations, actual_deviations)
        is_within_tolerance = self.benford_analysis_service.is_benford_distribution_within_tolerance(actual, 27)
        self.assertTrue(is_within_tolerance)

        expected = [29.63, 17.39, 12.6, 10.99, 7.78, 6.3, 5.54, 5.18, 4.59]
        actual = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(state_filter="TX"))
        self.assertEqual(expected, actual)
        expected_deviations = [1.56, 1.19, 0.8, 13.3, 1.52, 5.97, 4.48, 1.57, 0.22]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual)
        self.assertEqual(expected_deviations, actual_deviations)
        is_within_tolerance = self.benford_analysis_service.is_benford_distribution_within_tolerance(actual, 14)
        self.assertTrue(is_within_tolerance)

    def test_calculate_benford_distribution_by_year(self):
        expected = [28.39, 18.69, 13.44, 10.63, 8.04, 6.76, 4.93, 5.2, 3.92]
        actual = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(year_filter="2000"))
        self.assertEqual(expected, actual)
        expected_deviations = [5.68, 6.19, 7.52, 9.59, 1.77, 0.9, 15.0, 1.96, 14.78]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual)
        self.assertEqual(expected_deviations, actual_deviations)
        is_within_tolerance = self.benford_analysis_service.is_benford_distribution_within_tolerance(actual, 15)
        self.assertTrue(is_within_tolerance)

        expected = [28.58, 17.76, 12.97, 10.46, 8.7, 6.71, 5.71, 4.77, 4.34]
        actual = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(year_filter="2004"))
        self.assertEqual(expected, actual)
        expected_deviations = [5.05, 0.91, 3.76, 7.84, 10.13, 0.15, 1.55, 6.47, 5.65]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual)
        self.assertEqual(expected_deviations, actual_deviations)
        is_within_tolerance = self.benford_analysis_service.is_benford_distribution_within_tolerance(actual, 11)
        self.assertTrue(is_within_tolerance)

        expected = [28.46, 17.8, 13.02, 10.56, 8.32, 6.67, 5.88, 4.85, 4.44]
        actual = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(year_filter="2008"))
        self.assertEqual(expected, actual)
        expected_deviations = [5.45, 1.14, 4.16, 8.87, 5.32, 0.45, 1.38, 4.9, 3.48]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual)
        self.assertEqual(expected_deviations, actual_deviations)
        is_within_tolerance = self.benford_analysis_service.is_benford_distribution_within_tolerance(actual, 9)
        self.assertTrue(is_within_tolerance)

        expected = [28.83, 17.73, 12.96, 10.3, 8.25, 6.75, 5.34, 5.05, 4.78]
        actual = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(year_filter="2012"))
        self.assertEqual(expected, actual)
        expected_deviations = [4.22, 0.74, 3.68, 6.19, 4.43, 0.75, 7.93, 0.98, 3.91]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual)
        self.assertEqual(expected_deviations, actual_deviations)
        is_within_tolerance = self.benford_analysis_service.is_benford_distribution_within_tolerance(actual, 8)
        self.assertTrue(is_within_tolerance)

        expected = [29.67, 17.17, 12.99, 9.9, 8.05, 6.61, 6.16, 5.01, 4.44]
        actual = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(year_filter="2016"))
        self.assertEqual(expected, actual)
        expected_deviations = [1.43, 2.44, 3.92, 2.06, 1.9, 1.34, 6.21, 1.76, 3.48]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual)
        self.assertEqual(expected_deviations, actual_deviations)
        is_within_tolerance = self.benford_analysis_service.is_benford_distribution_within_tolerance(actual, 7)
        self.assertTrue(is_within_tolerance)

        expected = [29.02, 17.21, 11.72, 9.55, 7.44, 6.15, 5.28, 5.0, 8.62]
        actual = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(year_filter="2020"))
        self.assertEqual(expected, actual)
        expected_deviations = [3.59, 2.22, 6.24, 1.55, 5.82, 8.21, 8.97, 1.96, 87.39]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual)
        self.assertEqual(expected_deviations, actual_deviations)
        is_within_tolerance = self.benford_analysis_service.is_benford_distribution_within_tolerance(actual, 88)
        self.assertTrue(is_within_tolerance)


    def get_result_output_path(self):
        return self.get_results_directory() + "run-" + str(datetime.datetime.now()).replace(" ", "-").replace(":", "-") + ".csv"

    def get_results_directory(self):
        return self.get_resources_directory() + "results\\"

    def read_presidential_votes_state_data(self):
        return self.get_resources_directory() + "working_data\\presidential-votes-by-state-1976-2020-working.csv"

    def read_presidential_votes_county_data(self):
        return self.get_resources_directory() + "working_data\\presidential-votes-by-county-2000-2020-working.csv"

    def get_resources_directory(self):
        return self.get_test_directory() + "resources\\"

    def get_test_directory(self):
        return self.get_root_directory() + "test\\"

    def get_root_directory(self):
        return str(Path(os.path.realpath(__file__)).parent.parent) + "\\"


if __name__ == '__main__':
    unittest.main()
