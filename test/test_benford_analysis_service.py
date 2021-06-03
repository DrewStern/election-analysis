import unittest

from src.services.benford_analysis_service import BenfordAnalysisService
from src.services.election_result_service import ElectionResultService
from src.repositories.mock_election_result_repository import MockElectionResultRepository


class BenfordAnalysisServiceTestCases(unittest.TestCase):
    def setUp(self):
        self.mock_election_result_repository = MockElectionResultRepository()
        self.election_result_service = ElectionResultService(self.mock_election_result_repository)
        self.benford_analysis_service = BenfordAnalysisService(self.election_result_service)

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
        # candidates < locality < year == [(candidate, party)] < [(county, state)] < year


if __name__ == '__main__':
    unittest.main()
