import unittest

from src.data.models.election_event import ElectionEvent
from src.services.election_event_service import ElectionEventService
from src.services.election_result_service import ElectionResultService
from src.data.repositories.mock_election_result_repository import MockElectionResultRepository


class ElectionResultServiceTestCases(unittest.TestCase):
    def setUp(self) -> None:
        self.mock_election_result_repository = MockElectionResultRepository()
        self.election_result_service = ElectionResultService(self.mock_election_result_repository)
        self.election_event_service = ElectionEventService(self.election_result_service)

        self.test_events = [
            ElectionEvent("1993", "MO", "County 3"),
            ElectionEvent("1997", "FK", "County 1"),
            ElectionEvent("2001", "MO", "County 2"),
            ElectionEvent("2005", "FK", "County 3"),
        ]

    def test_get_winning_party_for_election(self):
        expected = ["Republican", "Democrat", "Republican", "Democrat"]
        for index in range(len(expected)):
            actual = self.election_result_service.get_winning_party_for_election(self.test_events[index])
            self.assertEqual(expected[index], actual)

    def test_get_party_ranking_for_election(self):
        expected = [
            ["Republican", "Republican", "Democrat"],
            ["Democrat", "Republican"],
            ["Republican", "Democrat"],
            ["Democrat", "Republican"]
        ]
        for index in range(len(expected)):
            actual = self.election_result_service.get_party_ranking_for_election(self.test_events[index])
            self.assertEqual(expected[index], actual)

    def test_get_winning_candidate_for_election(self):
        expected = ["Fake Candidate 3", "Fake Candidate 1", "Fake Candidate 2", "Fake Candidate 1"]
        for index in range(len(expected)):
            actual = self.election_result_service.get_winning_candidate_for_election(self.test_events[index])
            self.assertEqual(expected[index], actual)

    def test_get_candidate_ranking_for_election(self):
        expected = [
            ["Fake Candidate 3", "Fake Candidate 2", "Fake Candidate 1"],
            ["Fake Candidate 1", "Fake Candidate 2"],
            ["Fake Candidate 2", "Fake Candidate 1"],
            ["Fake Candidate 1", "Fake Candidate 2"]
        ]
        for index in range(len(expected)):
            actual = self.election_result_service.get_candidate_ranking_for_election(self.test_events[index])
            self.assertEqual(expected[index], actual)

    def test_get_ranked_election_results(self):
        pass

    def test_get_nationally_winning_candidate_by_year(self):
        expected = "Fake Candidate 1"
        actual = self.election_result_service.get_nationally_winning_candidate_by_year("1993")
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
