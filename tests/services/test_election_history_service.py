import unittest

from src.repositories.mock_election_result_repository import MockElectionResultRepository
from src.services.election_history_service import ElectionHistoryService
from src.services.election_result_service import ElectionResultService


class ElectionHistoryServiceTestCases(unittest.TestCase):
    def setUp(self) -> None:
        self.mock_election_repository = MockElectionResultRepository()
        self.election_result_service = ElectionResultService(self.mock_election_repository)
        self.election_history_service = ElectionHistoryService(self.election_result_service)

    def test_get_election_years(self):
        expected = ["1993", "1997", "2001", "2005"]
        actual = self.election_history_service.get_election_years()
        self.assertEqual(expected, actual)

    def test_get_winning_party_history_for_locality(self):
        expected = ["Republican", "Democrat"]
        actual = self.election_history_service.get_winning_party_history_for_locality("County 1,MO")
        self.assertEqual(expected, actual)

        expected = ["Democrat", "Republican"]
        actual = self.election_history_service.get_winning_party_history_for_locality("County 2,MO")
        self.assertEqual(expected, actual)

        expected = ["Republican", "Republican"]
        actual = self.election_history_service.get_winning_party_history_for_locality("County 3,MO")
        self.assertEqual(expected, actual)

    def test_get_winning_candidate_history_for_locality(self):
        expected = ["Fake Candidate 2", "Fake Candidate 1"]
        actual = self.election_history_service.get_winning_candidate_history_for_locality("County 1,MO")
        self.assertEqual(expected, actual)

        expected = ["Fake Candidate 1", "Fake Candidate 2"]
        actual = self.election_history_service.get_winning_candidate_history_for_locality("County 2,MO")
        self.assertEqual(expected, actual)

        expected = ["Fake Candidate 3", "Fake Candidate 2"]
        actual = self.election_history_service.get_winning_candidate_history_for_locality("County 3,MO")
        self.assertEqual(expected, actual)