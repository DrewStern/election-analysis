import unittest

from src.services.analysis.benford_analysis_service import BenfordAnalysisService
from src.services.election_result_service import ElectionResultService
from src.repositories.mock_election_result_repository import MockElectionResultRepository


# digit_occurrence_template = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
class BenfordAnalysisServiceTestCases(unittest.TestCase):
    def setUp(self):
        self.mock_election_result_repository = MockElectionResultRepository()
        self.election_result_service = ElectionResultService(self.mock_election_result_repository)
        self.benford_analysis_service = BenfordAnalysisService(self.election_result_service)

    def test_get_maximum_deviation_from_benford_distribution(self):
        given_distribution = self.benford_analysis_service.first_digit_benford_distribution
        expected = 0
        actual = self.benford_analysis_service.get_maximum_deviation_from_benford_distribution(given_distribution)
        self.assertEqual(expected, actual)

        given_distribution = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        expected = 100
        actual = self.benford_analysis_service.get_maximum_deviation_from_benford_distribution(given_distribution)
        self.assertEqual(expected, actual)

        # given_distribution chosen arbitrarily, then tolerance chosen around that
        given_distribution = [0, 30.0, 17.5, 12.9, 9.4, 7.8, 6.7, 5.5, 4.9, 4.1]
        expected = 10.87
        actual = self.benford_analysis_service.get_maximum_deviation_from_benford_distribution(given_distribution)
        self.assertEqual(expected, actual)

    def test_calculate_deviation_from_benford_distribution(self):
        given_distribution = self.benford_analysis_service.first_digit_benford_distribution
        expected = ["INF", 0, 0, 0, 0, 0, 0, 0, 0, 0]
        actual = self.benford_analysis_service.calculate_deviation_from_benford_distribution(given_distribution)
        self.assertEqual(expected, actual)

        # given_distribution = 1.1 * first_digit_benford_distribution
        given_distribution = [0, 33.11, 19.36, 13.75, 10.67, 8.69, 7.37, 6.38, 5.61, 5.06]
        expected = ["INF", 10, 10, 10, 10, 10, 10, 10, 10, 10]
        actual = self.benford_analysis_service.calculate_deviation_from_benford_distribution(given_distribution)
        self.assertEqual(expected, actual)

        # given_distribution = 0.50 * first_digit_benford_distribution
        given_distribution = [0, 15.05, 8.8, 6.25, 4.85, 3.95, 3.35, 2.9, 2.55, 2.3]
        expected = ["INF", 50, 50, 50, 50, 50, 50, 50, 50, 50]
        actual = self.benford_analysis_service.calculate_deviation_from_benford_distribution(given_distribution)
        self.assertEqual(expected, actual)

    def test_calculate_benford_distribution(self):
        expected = [0, 32, 0, 0, 24, 0, 32, 4, 0, 8]
        actual = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results())
        self.assertEqual(expected, actual)

        expected = [4, 4, 24, 0, 8, 12, 0, 0, 0, 48]
        actual = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(), 1)
        self.assertEqual(expected, actual)

    def test_calculate_benford_distribution_by_year(self):
        # year_1993_leading_digit_occurrences = [0, 1, 0, 0, 2, 0, 3, 1, 0, 0]
        expected = [0, 14.29, 0, 0, 28.57, 0, 42.86, 14.29, 0, 0]
        actual = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(year_filter="1993"))
        self.assertEqual(expected, actual)

        # year_1997_leading_digit_occurrences = [0, 3, 0, 0, 1, 0, 1, 0, 0, 1]
        expected = [0, 50.00, 0, 0, 16.67, 0, 16.67, 0, 0, 16.67]
        actual = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(year_filter="1997"))
        self.assertEqual(expected, actual)

        # year_2001_leading_digit_occurrences = [0, 1, 0, 0, 2, 0, 3, 0, 0, 0]
        expected = [0, 16.67, 0, 0, 33.33, 0, 50.00, 0, 0, 0]
        actual = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(year_filter="2001"))
        self.assertEqual(expected, actual)

        # year_2005_leading_digit_occurrences = [0, 3, 0, 0, 1, 0, 1, 0, 0, 1]
        expected = [0, 50.00, 0, 0, 16.67, 0, 16.67, 0, 0, 16.67]
        actual = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(year_filter="2005"))
        self.assertEqual(expected, actual)

    def test_calculate_benford_distribution_by_locality(self):
        # county1_mo_leading_digit_occurrences = [0, 2, 0, 0, 0, 0, 2, 0, 0, 0]
        expected = [0, 50.00, 0, 0, 0, 0, 50.00, 0, 0, 0]
        actual = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(county_filter="County 1", state_filter="MO"))
        self.assertEqual(expected, actual)

        # county2_mo_leading_digit_occurrences = [0, 0, 0, 0, 2, 0, 2, 0, 0, 0]
        expected = [0, 0, 0, 0, 50.00, 0, 50.00, 0, 0, 0]
        actual = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(county_filter="County 2", state_filter="MO"))
        self.assertEqual(expected, actual)

        # county3_mo_leading_digit_occurrences = [0, 0, 0, 0, 2, 0, 2, 1, 0, 0]
        expected = [0, 0, 0, 0, 40.00, 0, 40.00, 20.00, 0, 0]
        actual = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(county_filter="County 3", state_filter="MO"))
        self.assertEqual(expected, actual)

        # county1_fk_leading_digit_occurrences = [0, 4, 0, 0, 0, 0, 0, 0, 0, 0]
        expected = [0, 100.00, 0, 0, 0, 0, 0, 0, 0, 0]
        actual = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(county_filter="County 1", state_filter="FK"))
        self.assertEqual(expected, actual)

        # county2_fk_leading_digit_occurrences = [0, 2, 0, 0, 0, 0, 0, 0, 0, 2]
        expected = [0, 50.00, 0, 0, 0, 0, 0, 0, 0, 50.00]
        actual = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(county_filter="County 2", state_filter="FK"))
        self.assertEqual(expected, actual)

        # county3_fk_leading_digit_occurrences = [0, 0, 0, 0, 2, 0, 2, 0, 0, 0]
        expected = [0, 0, 0, 0, 50.00, 0, 50.00, 0, 0, 0]
        actual = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(county_filter="County 3", state_filter="FK"))
        self.assertEqual(expected, actual)

    def test_calculate_benford_distribution_by_candidate(self):
        # candidate_1_leading_digit_occurrences = [0, 4, 0, 0, 6, 0, 0, 0, 0, 2]
        expected = [0, 33.33, 0, 0, 50, 0, 0, 0, 0, 16.67]
        actual = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(candidate_filter="Fake Candidate 1"))
        self.assertEqual(expected, actual)

        # candidate_2_leading_digit_occurrences = [0, 4, 0, 0, 0, 0, 8, 0, 0, 0]
        expected = [0, 33.33, 0, 0, 0, 0, 66.67, 0, 0, 0]
        actual = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(candidate_filter="Fake Candidate 2"))
        self.assertEqual(expected, actual)

    def test_calculate_benford_distribution_by_party(self):
        # democrat_leading_digit_occurrences = [0, 4, 0, 0, 6, 0, 0, 0, 0, 2]
        expected = [0, 33.33, 0, 0, 50, 0, 0, 0, 0, 16.67]
        actual = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(party_filter="Democrat"))
        self.assertEqual(expected, actual)

        # this is an interesting case because we have Fake Candidate 3 here who's also running as a Republican
        # republican_leading_digit_occurrences = [0, 4, 0, 0, 0, 0, 8, 1, 0, 0]
        expected = [0, 30.77, 0, 0, 0, 0, 61.54, 7.69, 0, 0]
        actual = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(party_filter="Republican"))
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
