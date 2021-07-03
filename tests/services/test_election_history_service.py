import unittest

from src.repositories.mock_election_result_repository import MockElectionResultRepository
from src.services.election_event_service import ElectionEventService
from src.services.election_history_service import ElectionHistoryService
from src.services.election_result_service import ElectionResultService


class ElectionHistoryServiceTestCases(unittest.TestCase):
    def setUp(self) -> None:
        self.mock_election_repository = MockElectionResultRepository()
        self.election_result_service = ElectionResultService(self.mock_election_repository)
        self.election_event_service = ElectionEventService(self.election_result_service)
        self.election_history_service = ElectionHistoryService(self.election_event_service, self.election_result_service)

    def test_get_winning_party_history_for_locality(self):
        expected = {
            "1993": "Republican",
            "1997": "",
            "2001": "Democrat",
            "2005": "",
        }
        actual = self.election_history_service.get_winning_party_history_for_locality("County 1,MO")
        self.assertEqual(expected, actual)

        expected = {
            "1993": "Democrat",
            "1997": "",
            "2001": "Republican",
            "2005": "",
        }
        actual = self.election_history_service.get_winning_party_history_for_locality("County 2,MO")
        self.assertEqual(expected, actual)

        expected = {
            "1993": "Republican",
            "1997": "",
            "2001": "Republican",
            "2005": "",
        }
        actual = self.election_history_service.get_winning_party_history_for_locality("County 3,MO")
        self.assertEqual(expected, actual)

    def test_get_winning_candidate_history_for_locality(self):
        expected = {
            "1993": "Fake Candidate 2",
            "1997": "",
            "2001": "Fake Candidate 1",
            "2005": "",
        }
        actual = self.election_history_service.get_winning_candidate_history_for_locality("County 1,MO")
        self.assertEqual(expected, actual)

        expected = {
            "1993": "Fake Candidate 1",
            "1997": "",
            "2001": "Fake Candidate 2",
            "2005": "",
        }
        actual = self.election_history_service.get_winning_candidate_history_for_locality("County 2,MO")
        self.assertEqual(expected, actual)

        expected = {
            "1993": "Fake Candidate 3",
            "1997": "",
            "2001": "Fake Candidate 2",
            "2005": "",
        }
        actual = self.election_history_service.get_winning_candidate_history_for_locality("County 3,MO")
        self.assertEqual(expected, actual)