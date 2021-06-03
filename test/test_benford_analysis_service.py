import unittest

from src.services.benford_analysis_service import BenfordAnalysisService
from src.services.election_result_service import ElectionResultService
from src.repositories.mock_election_result_repository import MockElectionResultRepository


class BenfordAnalysisServiceTestCases(unittest.TestCase):
    def setUp(self):
        self.mock_election_result_repository = MockElectionResultRepository()
        self.election_result_service = ElectionResultService(self.mock_election_result_repository)
        self.benford_analysis_service = BenfordAnalysisService(self.election_result_service)

    def test_is_benford_distribution_within_tolerance(self):
        given_distribution = self.benford_analysis_service.expected_distribution
        is_within_tolerance = self.benford_analysis_service.is_benford_distribution_within_tolerance(given_distribution, 0.00001)
        self.assertTrue(is_within_tolerance)

        given_distribution = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        is_within_tolerance = self.benford_analysis_service.is_benford_distribution_within_tolerance(given_distribution, 99.9)
        self.assertFalse(is_within_tolerance)

        # given_distribution chosen arbitrarily, then tolerance chosen around that
        given_distribution = [30.0, 17.5, 12.9, 9.4, 7.8, 6.7, 5.5, 4.9, 4.1]
        is_within_tolerance = self.benford_analysis_service.is_benford_distribution_within_tolerance(given_distribution, 10.87)
        self.assertTrue(is_within_tolerance)
        is_within_tolerance = self.benford_analysis_service.is_benford_distribution_within_tolerance(given_distribution, 10.86)
        self.assertFalse(is_within_tolerance)

    def test_calculate_benford_distribution(self):
        expected = [32, 0, 0, 24, 0, 32, 4, 0, 8]
        actual = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results())
        self.assertEqual(expected, actual)

        # candidate_1_leading_digit_occurrences = [4, 0, 0, 6, 0, 0, 0, 0, 2]
        expected = [33.33, 0, 0, 50, 0, 0, 0, 0, 16.67]
        actual = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(candidate_filter="Fake Candidate 1"))
        self.assertEqual(expected, actual)

        # candidate_2_leading_digit_occurrences = [4, 0, 0, 0, 0, 8, 0, 0, 0]
        expected = [33.33, 0, 0, 0, 0, 66.67, 0, 0, 0]
        actual = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(candidate_filter="Fake Candidate 2"))
        self.assertEqual(expected, actual)

        # democrat_leading_digit_occurrences = [4, 0, 0, 6, 0, 0, 0, 0, 2]
        expected = [33.33, 0, 0, 50, 0, 0, 0, 0, 16.67]
        actual = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(party_filter="Democrat"))
        self.assertEqual(expected, actual)

        # this is an interesting case because we have Fake Candidate 3 here who's also running as a Republican
        # republican_leading_digit_occurrences = [4, 0, 0, 0, 0, 8, 1, 0, 0]
        expected = [30.77, 0, 0, 0, 0, 61.54, 7.69, 0, 0]
        actual = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(party_filter="Republican"))
        self.assertEqual(expected, actual)

        # template_leading_digit_occurrences = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        # note: localities differ from how candidates work, because
        # there will be multiple candidates per locality, so we will have some double counting
        # similar if we want to calculate benford distribution by years; we have strict ordering
        # candidates < localities < years ==
        # [(candidate, party)] < [(county, state)] < years


if __name__ == '__main__':
    unittest.main()
