import unittest

from src.election_result_service import ElectionResultService
from src.mock.mock_election_result_repository import MockElectionResultRepository


class ElectionResultServiceTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.election_result_service = ElectionResultService(MockElectionResultRepository())

    def test_get_election_winner(self):
        expected = "Fake Candidate 2"
        actual = self.election_result_service.get_election_winner("1993", "County 3", "MO")
        self.assertEqual(expected, actual)

        expected = "Fake Candidate 1"
        actual = self.election_result_service.get_election_winner("1997", "County 1", "FK")
        self.assertEqual(expected, actual)

        expected = "Fake Candidate 2"
        actual = self.election_result_service.get_election_winner("2001", "County 2", "MO")
        self.assertEqual(expected, actual)

        expected = "Fake Candidate 2"
        actual = self.election_result_service.get_election_winner("2005", "County 3", "FK")
        self.assertEqual(expected, actual)

    def test_get_election_ranking(self):
        expected = ["Fake Candidate 2", "Fake Candidate 1"]
        actual = self.election_result_service.get_election_ranking("1993", "County 3", "MO")
        self.assert_lists_equal(expected, actual)

        expected = ["Fake Candidate 1", "Fake Candidate 2"]
        actual = self.election_result_service.get_election_ranking("1997", "County 1", "FK")
        self.assert_lists_equal(expected, actual)

        expected = ["Fake Candidate 2", "Fake Candidate 1"]
        actual = self.election_result_service.get_election_ranking("2001", "County 2", "MO")
        self.assert_lists_equal(expected, actual)

        expected = ["Fake Candidate 2", "Fake Candidate 1"]
        actual = self.election_result_service.get_election_ranking("2005", "County 3", "FK")
        self.assert_lists_equal(expected, actual)

    def test_get_election_winner_using_invalid_data(self):
        expected = "Unknown"
        actual = self.election_result_service.get_election_winner("NoSuchYear", "County 3", "FK")
        self.assertEqual(expected, actual)

        expected = "Unknown"
        actual = self.election_result_service.get_election_winner("2005", "NoSuchCounty", "FK")
        self.assertEqual(expected, actual)

        expected = "Unknown"
        actual = self.election_result_service.get_election_winner("2005", "County 3", "NoSuchState")
        self.assertEqual(expected, actual)

    def test_get_nationally_winning_candidate_by_year(self):
        expected = "Fake Candidate 1"
        actual = self.election_result_service.get_nationally_winning_candidate_by_year("1993")
        self.assertEqual(expected, actual)

    def assert_lists_equal(self, list1, list2):
        self.assertEqual(len(list1), len(list2))
        for index in range(len(list1)):
            self.assertEqual(list1[index], list2[index].candidate)


if __name__ == '__main__':
    unittest.main()
