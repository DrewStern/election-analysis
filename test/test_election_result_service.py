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

    def test_get_election_winner_using_invalid_data(self):
        expected = "Unknown"
        actual = self.election_result_service.get_election_winner("nosuchyear", "County 3", "FK")
        self.assertEqual(expected, actual)

        expected = "Unknown"
        actual = self.election_result_service.get_election_winner("2005", "nosuchcounty", "FK")
        self.assertEqual(expected, actual)

        expected = "Unknown"
        actual = self.election_result_service.get_election_winner("2005", "County 3", "nosuchstate")
        self.assertEqual(expected, actual)

    def test_get_nationally_winning_candidate_by_year(self):
        expected = "Fake Candidate 1"
        actual = self.election_result_service.get_nationally_winning_candidate_by_year("1993")
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
