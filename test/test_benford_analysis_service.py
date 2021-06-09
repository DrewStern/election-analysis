import unittest

from src.services.benford_analysis_service import BenfordAnalysisService
from src.services.election_result_service import ElectionResultService
from src.repositories.mock_election_result_repository import MockElectionResultRepository


# template_leading_digit_occurrences = [0, 0, 0, 0, 0, 0, 0, 0, 0]
class BenfordAnalysisServiceTestCases(unittest.TestCase):
    def setUp(self):
        self.mock_election_result_repository = MockElectionResultRepository()
        self.election_result_service = ElectionResultService(self.mock_election_result_repository)
        self.benford_analysis_service = BenfordAnalysisService(self.election_result_service)

    def test_is_benford_distribution_within_tolerance(self):
        given_distribution = self.benford_analysis_service.expected_distribution
        is_within_tolerance = self.benford_analysis_service.is_benford_distribution_within_tolerance(given_distribution, 0)
        self.assertTrue(is_within_tolerance)

        given_distribution = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        is_within_tolerance = self.benford_analysis_service.is_benford_distribution_within_tolerance(given_distribution, 100)
        self.assertTrue(is_within_tolerance)
        is_within_tolerance = self.benford_analysis_service.is_benford_distribution_within_tolerance(given_distribution, 99.99)
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

    def test_calculate_benford_distribution_by_year(self):
        # year_1993_leading_digit_occurrences = [1, 0, 0, 2, 0, 3, 1, 0, 0]
        expected = [14.29, 0, 0, 28.57, 0, 42.86, 14.29, 0, 0]
        actual = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(year_filter="1993"))
        self.assertEqual(expected, actual)

        # year_1997_leading_digit_occurrences = [3, 0, 0, 1, 0, 1, 0, 0, 1]
        expected = [50.00, 0, 0, 16.67, 0, 16.67, 0, 0, 16.67]
        actual = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(year_filter="1997"))
        self.assertEqual(expected, actual)

        # year_2001_leading_digit_occurrences = [1, 0, 0, 2, 0, 3, 0, 0, 0]
        expected = [16.67, 0, 0, 33.33, 0, 50.00, 0, 0, 0]
        actual = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(year_filter="2001"))
        self.assertEqual(expected, actual)

        # year_2005_leading_digit_occurrences = [3, 0, 0, 1, 0, 1, 0, 0, 1]
        expected = [50.00, 0, 0, 16.67, 0, 16.67, 0, 0, 16.67]
        actual = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(year_filter="2005"))
        self.assertEqual(expected, actual)

    def test_calculate_benford_distribution_by_locality(self):
        # county1_mo_leading_digit_occurrences = [2, 0, 0, 0, 0, 2, 0, 0, 0]
        expected = [50.00, 0, 0, 0, 0, 50.00, 0, 0, 0]
        actual = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(county_filter="County 1", state_filter="MO"))
        self.assertEqual(expected, actual)

        # county2_mo_leading_digit_occurrences = [0, 0, 0, 2, 0, 2, 0, 0, 0]
        expected = [0, 0, 0, 50.00, 0, 50.00, 0, 0, 0]
        actual = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(county_filter="County 2", state_filter="MO"))
        self.assertEqual(expected, actual)

        # county3_mo_leading_digit_occurrences = [0, 0, 0, 2, 0, 2, 1, 0, 0]
        expected = [0, 0, 0, 40.00, 0, 40.00, 20.00, 0, 0]
        actual = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(county_filter="County 3", state_filter="MO"))
        self.assertEqual(expected, actual)

        # county1_fk_leading_digit_occurrences = [4, 0, 0, 0, 0, 0, 0, 0, 0]
        expected = [100.00, 0, 0, 0, 0, 0, 0, 0, 0]
        actual = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(county_filter="County 1", state_filter="FK"))
        self.assertEqual(expected, actual)

        # county2_fk_leading_digit_occurrences = [2, 0, 0, 0, 0, 0, 0, 0, 2]
        expected = [50.00, 0, 0, 0, 0, 0, 0, 0, 50.00]
        actual = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(county_filter="County 2", state_filter="FK"))
        self.assertEqual(expected, actual)

        # county3_fk_leading_digit_occurrences = [0, 0, 0, 2, 0, 2, 0, 0, 0]
        expected = [0, 0, 0, 50.00, 0, 50.00, 0, 0, 0]
        actual = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(county_filter="County 3", state_filter="FK"))
        self.assertEqual(expected, actual)

    def test_calculate_benford_distribution_by_candidate(self):
        # candidate_1_leading_digit_occurrences = [4, 0, 0, 6, 0, 0, 0, 0, 2]
        expected = [33.33, 0, 0, 50, 0, 0, 0, 0, 16.67]
        actual = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(candidate_filter="Fake Candidate 1"))
        self.assertEqual(expected, actual)

        # candidate_2_leading_digit_occurrences = [4, 0, 0, 0, 0, 8, 0, 0, 0]
        expected = [33.33, 0, 0, 0, 0, 66.67, 0, 0, 0]
        actual = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(candidate_filter="Fake Candidate 2"))
        self.assertEqual(expected, actual)

    def test_calculate_benford_distribution_by_party(self):
        # democrat_leading_digit_occurrences = [4, 0, 0, 6, 0, 0, 0, 0, 2]
        expected = [33.33, 0, 0, 50, 0, 0, 0, 0, 16.67]
        actual = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(party_filter="Democrat"))
        self.assertEqual(expected, actual)

        # this is an interesting case because we have Fake Candidate 3 here who's also running as a Republican
        # republican_leading_digit_occurrences = [4, 0, 0, 0, 0, 8, 1, 0, 0]
        expected = [30.77, 0, 0, 0, 0, 61.54, 7.69, 0, 0]
        actual = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(party_filter="Republican"))
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
