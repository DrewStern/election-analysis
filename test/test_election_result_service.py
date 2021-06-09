import unittest

from src.services.election_result_service import ElectionResultService
from src.repositories.mock_election_result_repository import MockElectionResultRepository


class ElectionResultServiceTestCases(unittest.TestCase):
    def setUp(self) -> None:
        self.mock_election_result_repository = MockElectionResultRepository()
        self.election_result_service = ElectionResultService(self.mock_election_result_repository)

    def test_get_winning_party_for_election(self):
        pass

    def test_get_party_ranking_for_election(self):
        pass

    def test_get_winning_candidate_for_election(self):
        expected = "Fake Candidate 3"
        actual = self.election_result_service.get_winning_candidate_for_election("1993", "County 3", "MO")
        self.assertEqual(expected, actual)

        expected = "Fake Candidate 1"
        actual = self.election_result_service.get_winning_candidate_for_election("1997", "County 1", "FK")
        self.assertEqual(expected, actual)

        expected = "Fake Candidate 2"
        actual = self.election_result_service.get_winning_candidate_for_election("2001", "County 2", "MO")
        self.assertEqual(expected, actual)

        expected = "Fake Candidate 1"
        actual = self.election_result_service.get_winning_candidate_for_election("2005", "County 3", "FK")
        self.assertEqual(expected, actual)

    def test_get_winning_candidate_for_election_using_invalid_data(self):
        expected = None
        actual = self.election_result_service.get_winning_candidate_for_election("NoSuchYear", "County 3", "FK")
        self.assertEqual(expected, actual)

        expected = None
        actual = self.election_result_service.get_winning_candidate_for_election("2005", "NoSuchCounty", "FK")
        self.assertEqual(expected, actual)

        expected = None
        actual = self.election_result_service.get_winning_candidate_for_election("2005", "County 3", "NoSuchState")
        self.assertEqual(expected, actual)

    def test_get_candidate_ranking_for_election(self):
        expected = ["Fake Candidate 3", "Fake Candidate 2", "Fake Candidate 1"]
        actual = self.election_result_service.get_candidate_ranking_for_election("1993", "County 3", "MO")
        self.assert_lists_equal(expected, actual)

        expected = ["Fake Candidate 1", "Fake Candidate 2"]
        actual = self.election_result_service.get_candidate_ranking_for_election("1997", "County 1", "FK")
        self.assert_lists_equal(expected, actual)

        expected = ["Fake Candidate 2", "Fake Candidate 1"]
        actual = self.election_result_service.get_candidate_ranking_for_election("2001", "County 2", "MO")
        self.assert_lists_equal(expected, actual)

        expected = ["Fake Candidate 1", "Fake Candidate 2"]
        actual = self.election_result_service.get_candidate_ranking_for_election("2005", "County 3", "FK")
        self.assert_lists_equal(expected, actual)

    def test_get_candidate_ranking_for_election_using_invalid_data(self):
        expected = []
        actual = self.election_result_service.get_candidate_ranking_for_election("NoSuchYear", "County 3", "FK")
        self.assertEqual(expected, actual)

        expected = []
        actual = self.election_result_service.get_candidate_ranking_for_election("2005", "NoSuchCounty", "FK")
        self.assertEqual(expected, actual)

        expected = []
        actual = self.election_result_service.get_candidate_ranking_for_election("2005", "County 3", "NoSuchState")
        self.assertEqual(expected, actual)

    def test_get_ranked_election_results(self):
        pass

    def test_get_election_years(self):
        expected = ["1993", "1997", "2001", "2005"]
        actual = self.election_result_service.get_election_years()
        self.assert_lists_equal(expected, actual)

    def test_get_nationally_winning_candidate_by_year(self):
        expected = "Fake Candidate 1"
        actual = self.election_result_service.get_nationally_winning_candidate_by_year("1993")
        self.assertEqual(expected, actual)

    def assert_lists_equal(self, list1, list2):
        self.assertEqual(len(list1), len(list2))
        for index in range(len(list1)):
            self.assertEqual(list1[index], list2[index])


if __name__ == '__main__':
    unittest.main()
