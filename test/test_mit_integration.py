import datetime
import os
import unittest
from pathlib import Path

from src.repositories.election_result_repository import ElectionResultRepository
from src.services.election_result_service import ElectionResultService
from src.services.benford_analysis_service import BenfordAnalysisService


# The expected values here are just copy/paste of the service outputs. They should be considered as documentation.
# I did not go through the data set to manually calculate and double check these values.
# However, the unit tests WERE manually calculated and verified. Which lends weight to the validity of these results.
class MitIntegrationTestCases(unittest.TestCase):
    def setUp(self) -> None:
        data_path = self.read_presidential_votes_county_data()
        self.election_result_repository = ElectionResultRepository(data_path)
        self.election_result_service = ElectionResultService(self.election_result_repository)
        self.benford_analysis_service = BenfordAnalysisService(self.election_result_service)

    def test_calculate_benford_distribution(self):
        expected_distribution = [0.99, 28.85, 17.68, 12.74, 10.17, 8.07, 6.57, 5.53, 4.98, 4.43]
        actual_distribution = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results())
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 4.15, 0.45, 1.92, 4.85, 2.15, 1.94, 4.66, 2.35, 3.7]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 4.85
        actual_max_dev = self.benford_analysis_service.get_maximum_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)

    def test_calculate_benford_distribution_by_candidate_AlGore(self):
        expected_distribution = [0, 28.62, 19.32, 12.66, 11.01, 8.15, 6.35, 4.89, 5.46, 3.55]
        actual_distribution = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(candidate_filter="Al Gore"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 4.92, 9.77, 1.28, 13.51, 3.16, 5.22, 15.69, 7.06, 22.83]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 22.83
        actual_max_dev = self.benford_analysis_service.get_maximum_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)

    def test_calculate_benford_distribution_by_candidate_GeorgeWBush(self):
        expected_distribution = [0, 28.48, 17.36, 13.72, 10.18, 8.25, 6.96, 5.77, 4.93, 4.35]
        actual_distribution = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(candidate_filter="George W. Bush"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 5.38, 1.36, 9.76, 4.95, 4.43, 3.88, 0.52, 3.33, 5.43]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 9.76
        actual_max_dev = self.benford_analysis_service.get_maximum_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)

    def test_calculate_benford_distribution_by_candidate_JohnKerry(self):
        expected_distribution = [0, 28.38, 18.83, 12.71, 10.81, 8.85, 6.66, 4.85, 4.63, 4.28]
        actual_distribution = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(candidate_filter="John Kerry"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 5.71, 6.99, 1.68, 11.44, 12.03, 0.6, 16.38, 9.22, 6.96]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 16.38
        actual_max_dev = self.benford_analysis_service.get_maximum_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)

    def test_calculate_benford_distribution_by_candidate_BarackObama(self):
        expected_distribution = [0, 28.64, 18.87, 13.2, 10.19, 7.77, 6.45, 5.55, 4.5, 4.83]
        actual_distribution = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(candidate_filter="Barack Obama"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 4.85, 7.22, 5.6, 5.05, 1.65, 3.73, 4.31, 11.76, 5.0]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 11.76
        actual_max_dev = self.benford_analysis_service.get_maximum_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)

    def test_calculate_benford_distribution_by_candidate_JohnMcCain(self):
        expected_distribution = [0, 28.47, 16.84, 12.78, 10.59, 8.85, 6.82, 5.74, 5.36, 4.57]
        actual_distribution = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(candidate_filter="John McCain"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 5.42, 4.32, 2.24, 9.18, 12.03, 1.79, 1.03, 5.1, 0.65]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 12.03
        actual_max_dev = self.benford_analysis_service.get_maximum_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)

    def test_calculate_benford_distribution_by_candidate_MittRomney(self):
        expected_distribution = [0, 28.83, 16.48, 12.77, 10.74, 8.78, 7.13, 5.61, 5.45, 4.21]
        actual_distribution = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(candidate_filter="Mitt Romney"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 4.22, 6.36, 2.16, 10.72, 11.14, 6.42, 3.28, 6.86, 8.48]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 11.14
        actual_max_dev = self.benford_analysis_service.get_maximum_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)

    def test_calculate_benford_distribution_by_candidate_HillaryClinton(self):
        expected_distribution = [0, 29.91, 18.31, 13.62, 9.57, 6.91, 6.34, 6.4, 4.47, 4.47]
        actual_distribution = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(candidate_filter="Hillary Clinton"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 0.63, 4.03, 8.96, 1.34, 12.53, 5.37, 10.34, 12.35, 2.83]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 12.53
        actual_max_dev = self.benford_analysis_service.get_maximum_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)

        # Note that this references Trump's 2016 results
    def test_calculate_benford_distribution_by_candidate_DonaldTrump_2016(self):
        expected_distribution = [0, 29.44, 16.03, 12.36, 10.23, 9.19, 6.88, 5.93, 5.54, 4.4]
        actual_distribution = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(candidate_filter="Donald Trump"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 2.19, 8.92, 1.12, 5.46, 16.33, 2.69, 2.24, 8.63, 4.35]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 16.33
        actual_max_dev = self.benford_analysis_service.get_maximum_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)

        # Note that this references Trump's 2020 results
    def test_calculate_benford_distribution_by_candidate_DonaldTrump_2020(self):
        expected_distribution = [3.79, 29.49, 17.31, 11.2, 9.11, 7.7, 6.23, 5.41, 5.02, 4.73]
        actual_distribution = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(candidate_filter="Donald J Trump"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 2.03, 1.65, 10.4, 6.08, 2.53, 7.01, 6.72, 1.57, 2.83]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 10.4
        actual_max_dev = self.benford_analysis_service.get_maximum_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)

    def test_calculate_benford_distribution_by_candidate_JoeBiden(self):
        expected_distribution = [4.33, 28.55, 17.11, 12.25, 9.99, 7.17, 6.07, 5.15, 4.98, 4.39]
        actual_distribution = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(candidate_filter="Joseph R Biden Jr"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 5.15, 2.78, 2.0, 2.99, 9.24, 9.4, 11.21, 2.35, 4.57]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 11.21
        actual_max_dev = self.benford_analysis_service.get_maximum_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)

    def test_calculate_benford_distribution_by_party_Democrat(self):
        expected_distribution = [1.06, 28.77, 18.42, 12.88, 10.27, 7.71, 6.36, 5.37, 4.78, 4.39]
        actual_distribution = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(party_filter="Democrat"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 4.42, 4.66, 3.04, 5.88, 2.41, 5.07, 7.41, 6.27, 4.57]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 7.41
        actual_max_dev = self.benford_analysis_service.get_maximum_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)

    def test_calculate_benford_distribution_by_party_Republican(self):
        expected_distribution = [0.93, 28.92, 16.94, 12.61, 10.07, 8.43, 6.77, 5.68, 5.19, 4.46]
        actual_distribution = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(party_filter="Republican"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 3.92, 3.75, 0.88, 3.81, 6.71, 1.04, 2.07, 1.76, 3.04]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 6.71
        actual_max_dev = self.benford_analysis_service.get_maximum_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)

    def test_calculate_benford_distribution_by_state_AL(self):
        expected_distribution = [0, 26.24, 12.94, 14.05, 12.69, 11.82, 7.21, 5.22, 4.98, 4.85]
        actual_distribution = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(state_filter="AL"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 12.82, 26.48, 12.4, 30.82, 49.62, 7.61, 10.0, 2.35, 5.43]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 49.62
        actual_max_dev = self.benford_analysis_service.get_maximum_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)

    def test_calculate_benford_distribution_by_state_AK(self):
        expected_distribution = [0, 13.28, 21.16, 20.33, 19.5, 12.03, 6.85, 3.94, 2.07, 0.83]
        actual_distribution = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(state_filter="AK"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 55.88, 20.23, 62.64, 101.03, 52.28, 2.24, 32.07, 59.41, 81.96]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 101.03
        actual_max_dev = self.benford_analysis_service.get_maximum_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)

    def test_calculate_benford_distribution_by_state_AR(self):
        expected_distribution = [3.63, 28.96, 21.04, 13.78, 10.52, 5.93, 5.26, 3.63, 3.93, 3.33]
        actual_distribution = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(state_filter="AR"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 3.79, 19.55, 10.24, 8.45, 24.94, 21.49, 37.41, 22.94, 27.61]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 37.41
        actual_max_dev = self.benford_analysis_service.get_maximum_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)

    def test_calculate_benford_distribution_by_state_AZ(self):
        expected_distribution = [0, 33.75, 19.58, 12.08, 6.25, 5.42, 6.67, 7.92, 5.83, 2.5]
        actual_distribution = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(state_filter="AZ"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 12.13, 11.25, 3.36, 35.57, 31.39, 0.45, 36.55, 14.31, 45.65]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 45.65
        actual_max_dev = self.benford_analysis_service.get_maximum_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)

    def test_calculate_benford_distribution_by_state_CA(self):
        expected_distribution = [0, 26.72, 18.82, 13.36, 9.48, 9.2, 7.04, 5.6, 4.89, 4.89]
        actual_distribution = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(state_filter="CA"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 11.23, 6.93, 6.88, 2.27, 16.46, 5.07, 3.45, 4.12, 6.3]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 16.46
        actual_max_dev = self.benford_analysis_service.get_maximum_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)

    def test_calculate_benford_distribution_by_state_CO(self):
        expected_distribution = [0, 30.94, 15.54, 14.49, 10.31, 7.83, 6.4, 4.96, 4.31, 5.22]
        actual_distribution = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(state_filter="CO"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 2.79, 11.7, 15.92, 6.29, 0.89, 4.48, 14.48, 15.49, 13.48]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 15.92
        actual_max_dev = self.benford_analysis_service.get_maximum_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)

    def test_calculate_benford_distribution_by_state_CT(self):
        expected_distribution = [0, 25.0, 29.17, 13.54, 16.67, 9.38, 4.17, 2.08, 0.0, 0.0]
        actual_distribution = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(state_filter="CT"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 16.94, 65.74, 8.32, 71.86, 18.73, 37.76, 64.14, 100.0, 100.0]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 100.0
        actual_max_dev = self.benford_analysis_service.get_maximum_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)

    def test_calculate_benford_distribution_by_state_DE(self):
        expected_distribution = [0, 16.67, 13.89, 27.78, 13.89, 5.56, 2.78, 8.33, 8.33, 2.78]
        actual_distribution = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(state_filter="DE"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 44.62, 21.08, 122.24, 43.2, 29.62, 58.51, 43.62, 63.33, 39.57]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 122.24
        actual_max_dev = self.benford_analysis_service.get_maximum_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)

    def test_calculate_benford_distribution_by_state_FL(self):
        expected_distribution = [0, 26.37, 19.15, 12.06, 10.95, 8.58, 8.46, 5.47, 5.35, 3.61]
        actual_distribution = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(state_filter="FL"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 12.39, 8.81, 3.52, 12.89, 8.61, 26.27, 5.69, 4.9, 21.52]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 26.27
        actual_max_dev = self.benford_analysis_service.get_maximum_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)

    def test_calculate_benford_distribution_by_state_GA(self):
        expected_distribution = [2.9, 29.77, 19.5, 11.74, 9.08, 7.48, 6.04, 4.61, 5.07, 3.81]
        actual_distribution = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(state_filter="GA"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 1.1, 10.8, 6.08, 6.39, 5.32, 9.85, 20.52, 0.59, 17.17]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 20.52
        actual_max_dev = self.benford_analysis_service.get_maximum_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)

    def test_calculate_benford_distribution_by_state_HI(self):
        expected_distribution = [0, 41.67, 22.92, 8.33, 6.25, 4.17, 6.25, 2.08, 4.17, 4.17]
        actual_distribution = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(state_filter="HI"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 38.44, 30.23, 33.36, 35.57, 47.22, 6.72, 64.14, 18.24, 9.35]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 64.14
        actual_max_dev = self.benford_analysis_service.get_maximum_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)

    def test_calculate_benford_distribution_by_state_ID(self):
        expected_distribution = [0, 32.01, 17.23, 12.12, 10.23, 7.39, 6.44, 5.11, 5.3, 4.17]
        actual_distribution = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(state_filter="ID"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 6.35, 2.1, 3.04, 5.46, 6.46, 3.88, 11.9, 3.92, 9.35]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 11.9
        actual_max_dev = self.benford_analysis_service.get_maximum_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)

    def test_calculate_benford_distribution_by_state_IL(self):
        expected_distribution = [0, 29.17, 15.28, 13.15, 11.11, 9.56, 7.03, 4.33, 4.9, 5.47]
        actual_distribution = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(state_filter="IL"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 3.09, 13.18, 5.2, 14.54, 21.01, 4.93, 25.34, 3.92, 18.91]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 25.34
        actual_max_dev = self.benford_analysis_service.get_maximum_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)

    def test_calculate_benford_distribution_by_state_IN(self):
        expected_distribution = [0, 23.1, 19.02, 15.4, 11.59, 8.61, 6.43, 5.53, 5.16, 5.16]
        actual_distribution = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(state_filter="IN"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 23.26, 8.07, 23.2, 19.48, 8.99, 4.03, 4.66, 1.18, 12.17]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 23.26
        actual_max_dev = self.benford_analysis_service.get_maximum_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)

    def test_calculate_benford_distribution_by_state_IA(self):
        expected_distribution = [0, 24.1, 25.32, 15.3, 13.78, 7.58, 3.82, 3.17, 3.25, 3.68]
        actual_distribution = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(state_filter="IA"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 19.93, 43.86, 22.4, 42.06, 4.05, 42.99, 45.34, 36.27, 20.0]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 45.34
        actual_max_dev = self.benford_analysis_service.get_maximum_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)

    def test_calculate_benford_distribution_by_state_KS(self):
        expected_distribution = [0, 31.35, 20.48, 13.17, 7.86, 5.87, 5.79, 5.63, 5.24, 4.6]
        actual_distribution = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(state_filter="KS"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 4.15, 16.36, 5.36, 18.97, 25.7, 13.58, 2.93, 2.75, 0.0]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 25.7
        actual_max_dev = self.benford_analysis_service.get_maximum_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)

    def test_calculate_benford_distribution_by_state_KY(self):
        expected_distribution = [0, 30.9, 17.78, 12.36, 11.6, 7.78, 6.32, 5.56, 4.31, 3.4]
        actual_distribution = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(state_filter="KY"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 2.66, 1.02, 1.12, 19.59, 1.52, 5.67, 4.14, 15.49, 26.09]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 26.09
        actual_max_dev = self.benford_analysis_service.get_maximum_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)

    def test_calculate_benford_distribution_by_state_LA(self):
        expected_distribution = [0, 24.09, 15.62, 15.89, 7.55, 10.94, 8.72, 7.29, 5.21, 4.69]
        actual_distribution = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(state_filter="LA"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 19.97, 11.25, 27.12, 22.16, 38.48, 30.15, 25.69, 2.16, 1.96]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 38.48
        actual_max_dev = self.benford_analysis_service.get_maximum_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)

    def test_calculate_benford_distribution_by_state_MA(self):
        expected_distribution = [0, 41.67, 22.02, 2.98, 7.14, 10.71, 2.98, 6.55, 2.38, 3.57]
        actual_distribution = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(state_filter="MA"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 38.44, 25.11, 76.16, 26.39, 35.57, 55.52, 12.93, 53.33, 22.39]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 76.16
        actual_max_dev = self.benford_analysis_service.get_maximum_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)

    def test_calculate_benford_distribution_by_state_MD(self):
        expected_distribution = [0, 28.75, 20.0, 11.04, 10.83, 10.0, 3.75, 5.62, 5.21, 4.79]
        actual_distribution = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(state_filter="MD"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 4.49, 13.64, 11.68, 11.65, 26.58, 44.03, 3.1, 2.16, 4.13]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 44.03
        actual_max_dev = self.benford_analysis_service.get_maximum_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)

    def test_calculate_benford_distribution_by_state_ME(self):
        expected_distribution = [0, 40.1, 7.81, 10.94, 7.29, 6.25, 4.69, 5.73, 8.33, 8.85]
        actual_distribution = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(state_filter="ME"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 33.22, 55.63, 12.48, 24.85, 20.89, 30.0, 1.21, 63.33, 92.39]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 92.39
        actual_max_dev = self.benford_analysis_service.get_maximum_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)

    def test_calculate_benford_distribution_by_state_MI(self):
        expected_distribution = [0, 23.09, 17.77, 12.45, 9.44, 9.54, 9.44, 7.63, 6.22, 4.42]
        actual_distribution = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(state_filter="MI"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 23.29, 0.97, 0.4, 2.68, 20.76, 40.9, 31.55, 21.96, 3.91]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 40.9
        actual_max_dev = self.benford_analysis_service.get_maximum_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)

    def test_calculate_benford_distribution_by_state_MN(self):
        expected_distribution = [0, 29.98, 16.67, 12.26, 10.15, 6.99, 7.76, 5.17, 5.75, 5.27]
        actual_distribution = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(state_filter="MN"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 0.4, 5.28, 1.92, 4.64, 11.52, 15.82, 10.86, 12.75, 14.57]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 15.82
        actua_max_dev = self.benford_analysis_service.get_maximum_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_max_dev, actua_max_dev)

    def test_calculate_benford_distribution_by_state_MO(self):
        expected_distribution = [0, 28.2, 18.35, 14.24, 11.22, 8.85, 6.04, 5.4, 3.31, 4.39]
        actual_distribution = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(state_filter="MO"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 6.31, 4.26, 13.92, 15.67, 12.03, 9.85, 6.9, 35.1, 4.57]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 35.1
        actual_max_dev = self.benford_analysis_service.get_maximum_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)

    def test_calculate_benford_distribution_by_state_MS(self):
        expected_distribution = [0, 22.26, 16.77, 14.84, 14.33, 8.84, 7.62, 6.81, 4.88, 3.66]
        actual_distribution = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(state_filter="MS"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 26.05, 4.72, 18.72, 47.73, 11.9, 13.73, 17.41, 4.31, 20.43]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 47.73
        actual_max_dev = self.benford_analysis_service.get_maximum_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)

    def test_calculate_benford_distribution_by_state_MT(self):
        expected_distribution = [0, 34.97, 18.3, 14.14, 7.44, 5.51, 6.1, 6.1, 4.32, 3.12]
        actual_distribution = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(state_filter="MT"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 16.18, 3.98, 13.12, 23.3, 30.25, 8.96, 5.17, 15.29, 32.17]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 32.17
        actual_max_dev = self.benford_analysis_service.get_maximum_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)

    def test_calculate_benford_distribution_by_state_NC(self):
        expected_distribution = [0.17, 31.0, 17.72, 11.61, 9.33, 8.5, 6.22, 5.94, 4.33, 5.17]
        actual_distribution = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(state_filter="NC"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 2.99, 0.68, 7.12, 3.81, 7.59, 7.16, 2.41, 15.1, 12.39]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 15.1
        actual_max_dev = self.benford_analysis_service.get_maximum_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)

    def test_calculate_benford_distribution_by_state_ND(self):
        expected_distribution = [0, 33.02, 15.88, 11.95, 7.23, 5.82, 6.92, 6.13, 7.7, 5.35]
        actual_distribution = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(state_filter="ND"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 9.7, 9.77, 4.4, 25.46, 26.33, 3.28, 5.69, 50.98, 16.3]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 50.98
        actual_max_dev = self.benford_analysis_service.get_maximum_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)

    def test_calculate_benford_distribution_by_state_NE(self):
        expected_distribution = [0, 24.73, 20.88, 15.14, 9.95, 6.72, 5.91, 5.2, 6.54, 4.93]
        actual_distribution = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(state_filter="NE"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 17.84, 18.64, 21.12, 2.58, 14.94, 11.79, 10.34, 28.24, 7.17]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 28.24
        actual_max_dev = self.benford_analysis_service.get_maximum_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)

    def test_calculate_benford_distribution_by_state_NH(self):
        expected_distribution = [0, 40.83, 13.33, 12.5, 4.17, 0.0, 5.0, 5.0, 8.33, 10.83]
        actual_distribution = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(state_filter="NH"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 35.65, 24.26, 0.0, 57.01, 100.0, 25.37, 13.79, 63.33, 135.43]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 135.43
        actual_max_dev = self.benford_analysis_service.get_maximum_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)

    def test_calculate_benford_distribution_by_state_NJ(self):
        expected_distribution = [0, 38.89, 19.44, 5.56, 5.95, 4.37, 9.92, 6.75, 5.56, 3.57]
        actual_distribution = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(state_filter="NJ"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 29.2, 10.45, 55.52, 38.66, 44.68, 48.06, 16.38, 9.02, 22.39]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 55.52
        actual_max_dev = self.benford_analysis_service.get_maximum_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)

    def test_calculate_benford_distribution_by_state_NM(self):
        expected_distribution = [0, 29.8, 17.17, 17.42, 8.84, 9.09, 6.57, 3.28, 3.03, 4.8]
        actual_distribution = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(state_filter="NM"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 1.0, 2.44, 39.36, 8.87, 15.06, 1.94, 43.45, 40.59, 4.35]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 43.45
        actual_max_dev = self.benford_analysis_service.get_maximum_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)

    def test_calculate_benford_distribution_by_state_NV(self):
        expected_distribution = [0, 38.73, 9.31, 10.78, 6.86, 6.86, 6.37, 7.35, 5.88, 7.84]
        actual_distribution = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(state_filter="NV"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 28.67, 47.1, 13.76, 29.28, 13.16, 4.93, 26.72, 15.29, 70.43]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 70.43
        actual_max_dev = self.benford_analysis_service.get_maximum_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)

    def test_calculate_benford_distribution_by_state_NY(self):
        expected_distribution = [0, 37.63, 14.38, 9.27, 8.2, 7.12, 6.45, 4.7, 5.65, 6.59]
        actual_distribution = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(state_filter="NY"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 25.02, 18.3, 25.84, 15.46, 9.87, 3.73, 18.97, 10.78, 43.26]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 43.26
        actual_max_dev = self.benford_analysis_service.get_maximum_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)

    def test_calculate_benford_distribution_by_state_OH(self):
        expected_distribution = [0, 33.62, 12.97, 12.12, 9.94, 7.48, 7.95, 6.63, 4.92, 4.36]
        actual_distribution = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(state_filter="OH"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 11.69, 26.31, 3.04, 2.47, 5.32, 18.66, 14.31, 3.53, 5.22]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 26.31
        actual_max_dev = self.benford_analysis_service.get_maximum_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)

    def test_calculate_benford_distribution_by_state_OK(self):
        expected_distribution = [0, 34.17, 16.8, 11.77, 8.28, 7.79, 6.66, 5.36, 4.38, 4.79]
        actual_distribution = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(state_filter="OK"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 13.52, 4.55, 5.84, 14.64, 1.39, 0.6, 7.59, 14.12, 4.13]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 14.64
        actual_max_dev = self.benford_analysis_service.get_maximum_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)

    def test_calculate_benford_distribution_by_state_OR(self):
        expected_distribution = [0, 25.93, 17.59, 12.27, 6.94, 7.64, 9.49, 8.1, 8.33, 3.7]
        actual_distribution = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(state_filter="OR"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 13.85, 0.06, 1.84, 28.45, 3.29, 41.64, 39.66, 63.33, 19.57]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 63.33
        actual_max_dev = self.benford_analysis_service.get_maximum_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)

    def test_calculate_benford_distribution_by_state_PA(self):
        expected_distribution = [0, 33.96, 13.56, 9.33, 9.2, 9.2, 8.83, 6.59, 5.1, 4.23]
        actual_distribution = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(state_filter="PA"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 12.82, 22.95, 25.36, 5.15, 16.46, 31.79, 13.62, 0.0, 8.04]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 31.79
        actual_max_dev = self.benford_analysis_service.get_maximum_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)

    def test_calculate_benford_distribution_by_state_RI(self):
        expected_distribution = [0, 32.26, 22.58, 14.52, 11.29, 0.0, 1.61, 1.61, 8.06, 8.06]
        actual_distribution = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(state_filter="RI"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 7.18, 28.3, 16.16, 16.39, 100.0, 75.97, 72.24, 58.04, 75.22]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 100.0
        actual_max_dev = self.benford_analysis_service.get_maximum_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)

    def test_calculate_benford_distribution_by_state_SC(self):
        expected_distribution = [7.81, 23.91, 17.09, 12.15, 9.78, 9.49, 6.23, 6.03, 3.95, 3.56]
        actual_distribution = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(state_filter="SC"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 20.56, 2.9, 2.8, 0.82, 20.13, 7.01, 3.97, 22.55, 22.61]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 22.61
        actual_max_dev = self.benford_analysis_service.get_maximum_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)

    def test_calculate_benford_distribution_by_state_SD(self):
        expected_distribution = [0, 29.8, 16.79, 10.35, 9.72, 7.58, 7.7, 7.32, 4.67, 6.06]
        actual_distribution = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(state_filter="SD"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 1.0, 4.6, 17.2, 0.21, 4.05, 14.93, 26.21, 8.43, 31.74]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 31.74
        actual_max_dev = self.benford_analysis_service.get_maximum_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)

    def test_calculate_benford_distribution_by_state_TN(self):
        expected_distribution = [0, 30.18, 15.79, 11.49, 10.7, 9.91, 7.02, 5.44, 5.53, 3.95]
        actual_distribution = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(state_filter="TN"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 0.27, 10.28, 8.08, 10.31, 25.44, 4.78, 6.21, 8.43, 14.13]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 25.44
        actual_max_dev = self.benford_analysis_service.get_maximum_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)

    def test_calculate_benford_distribution_by_state_TX(self):
        expected_distribution = [0, 29.63, 17.39, 12.6, 10.99, 7.78, 6.3, 5.54, 5.18, 4.59]
        actual_distribution = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(state_filter="TX"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 1.56, 1.19, 0.8, 13.3, 1.52, 5.97, 4.48, 1.57, 0.22]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 13.3
        actual_max_dev = self.benford_analysis_service.get_maximum_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)

    def test_calculate_benford_distribution_by_state_UT(self):
        expected_distribution = [32.31, 20.19, 11.54, 8.08, 5.96, 5.19, 5.96, 4.42, 2.88, 3.46]
        actual_distribution = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(state_filter="UT"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 32.92, 34.43, 35.36, 38.56, 34.3, 11.04, 23.79, 43.53, 24.78]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 43.53
        actual_max_dev = self.benford_analysis_service.get_maximum_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)

    def test_calculate_benford_distribution_by_state_VA(self):
        expected_distribution = [1.55, 24.98, 19.35, 12.79, 9.84, 8.62, 6.51, 6.0, 6.14, 4.22]
        actual_distribution = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(state_filter="VA"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 17.01, 9.94, 2.32, 1.44, 9.11, 2.84, 3.45, 20.39, 8.26]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 20.39
        actual_max_dev = self.benford_analysis_service.get_maximum_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)

    def test_calculate_benford_distribution_by_state_VT(self):
        expected_distribution = [0, 36.36, 9.09, 2.6, 4.55, 16.23, 7.14, 10.39, 8.44, 5.19]
        actual_distribution = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(state_filter="VT"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 20.8, 48.35, 79.2, 53.09, 105.44, 6.57, 79.14, 65.49, 12.83]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 105.44
        actual_max_dev = self.benford_analysis_service.get_maximum_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)

    def test_calculate_benford_distribution_by_state_WA(self):
        expected_distribution = [0, 36.11, 13.68, 8.76, 9.83, 6.62, 7.05, 5.13, 5.56, 7.26]
        actual_distribution = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(state_filter="WA"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 19.97, 22.27, 29.92, 1.34, 16.2, 5.22, 11.55, 9.02, 57.83]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 57.83
        actual_max_dev = self.benford_analysis_service.get_maximum_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)

    def test_calculate_benford_distribution_by_state_WI(self):
        expected_distribution = [0, 27.08, 14.24, 16.55, 13.43, 8.68, 5.44, 5.32, 5.32, 3.94]
        actual_distribution = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(state_filter="WI"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 10.03, 19.09, 32.4, 38.45, 9.87, 18.81, 8.28, 4.31, 14.35]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 38.45
        actual_max_dev = self.benford_analysis_service.get_maximum_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)

    def test_calculate_benford_distribution_by_state_WV(self):
        expected_distribution = [0, 29.24, 19.85, 10.76, 10.61, 7.88, 5.61, 7.27, 5.0, 3.79]
        actual_distribution = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(state_filter="WV"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 2.86, 12.78, 13.92, 9.38, 0.25, 16.27, 25.34, 1.96, 17.61]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 25.34
        actual_max_dev = self.benford_analysis_service.get_maximum_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)

    def test_calculate_benford_distribution_by_state_WY(self):
        expected_distribution = [0, 28.99, 14.86, 13.77, 11.59, 8.33, 7.25, 5.8, 5.43, 3.99]
        actual_distribution = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(state_filter="WY"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 3.69, 15.57, 10.16, 19.48, 5.44, 8.21, 0.0, 6.47, 13.26]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 19.48
        actual_max_dev = self.benford_analysis_service.get_maximum_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)

    def test_calculate_benford_distribution_by_year_2000(self):
        expected_distribution = [0, 28.39, 18.69, 13.44, 10.63, 8.04, 6.76, 4.93, 5.2, 3.92]
        actual_distribution = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(year_filter="2000"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 5.68, 6.19, 7.52, 9.59, 1.77, 0.9, 15.0, 1.96, 14.78]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 15.0
        actual_max_dev = self.benford_analysis_service.get_maximum_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)

    def test_calculate_benford_distribution_by_year_2004(self):
        expected_distribution = [0, 28.58, 17.76, 12.97, 10.46, 8.7, 6.71, 5.71, 4.77, 4.34]
        actual_distribution = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(year_filter="2004"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 5.05, 0.91, 3.76, 7.84, 10.13, 0.15, 1.55, 6.47, 5.65]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 10.13
        actual_max_dev = self.benford_analysis_service.get_maximum_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)

    def test_calculate_benford_distribution_by_year_2008(self):
        expected_distribution = [0, 28.46, 17.8, 13.02, 10.56, 8.32, 6.67, 5.88, 4.85, 4.44]
        actual_distribution = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(year_filter="2008"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 5.45, 1.14, 4.16, 8.87, 5.32, 0.45, 1.38, 4.9, 3.48]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 8.87
        actual_max_dev = self.benford_analysis_service.get_maximum_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)

    def test_calculate_benford_distribution_by_year_2012(self):
        expected_distribution = [0, 28.83, 17.73, 12.96, 10.3, 8.25, 6.75, 5.34, 5.05, 4.78]
        actual_distribution = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(year_filter="2012"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 4.22, 0.74, 3.68, 6.19, 4.43, 0.75, 7.93, 0.98, 3.91]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 7.93
        actual_max_dev = self.benford_analysis_service.get_maximum_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)

    def test_calculate_benford_distribution_by_year_2016(self):
        expected_distribution = [0, 29.67, 17.17, 12.99, 9.9, 8.05, 6.61, 6.16, 5.01, 4.44]
        actual_distribution = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(year_filter="2016"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 1.43, 2.44, 3.92, 2.06, 1.9, 1.34, 6.21, 1.76, 3.48]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 6.21
        actual_max_dev = self.benford_analysis_service.get_maximum_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)

    def test_calculate_benford_distribution_by_year_2020(self):
        expected_distribution = [4.06, 29.02, 17.21, 11.72, 9.55, 7.44, 6.15, 5.28, 5.0, 4.56]
        actual_distribution = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(year_filter="2020"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 3.59, 2.22, 6.24, 1.55, 5.82, 8.21, 8.97, 1.96, 0.87]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 8.97
        actual_max_dev = self.benford_analysis_service.get_maximum_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)

    def get_result_output_path(self):
        return self.get_results_directory() + "run-" + str(datetime.datetime.now()).replace(" ", "-").replace(":", "-") + ".csv"

    def get_results_directory(self):
        return self.get_test_data_directory() + "results\\"

    def read_presidential_votes_state_data(self):
        return self.get_working_test_data_directory() + "presidential-votes-by-state-1976-2020.csv"

    def read_presidential_votes_county_data(self):
        return self.get_working_test_data_directory() + "presidential-votes-by-county-2000-2020.csv"

    def get_working_test_data_directory(self):
        return self.get_test_data_directory() + "working\\"

    def get_test_data_directory(self):
        return self.get_test_directory() + "data\\"

    def get_test_directory(self):
        return self.get_root_directory() + "test\\"

    def get_root_directory(self):
        return str(Path(os.path.realpath(__file__)).parent.parent) + "\\"


if __name__ == '__main__':
    unittest.main()
