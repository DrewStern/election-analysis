import unittest

from src.repositories.mock_election_result_repository import MockElectionResultRepository
from src.services.election_result_service import ElectionResultService
from src.services.locality_result_service import LocalityResultService


class LocalityResultServiceTestCases(unittest.TestCase):
    def setUp(self) -> None:
        self.mock_election_result_repository = MockElectionResultRepository()
        self.election_result_service = ElectionResultService(self.mock_election_result_repository)
        self.locality_result_service = LocalityResultService(self.election_result_service)

    def test_get_winning_party_history_for_locality(self):
        expected = ["Republican", "Democrat"]
        actual = self.locality_result_service.get_winning_party_history_for_locality("County 1,MO")
        self.assertEqual(expected, actual)

        expected = ["Democrat", "Republican"]
        actual = self.locality_result_service.get_winning_party_history_for_locality("County 2,MO")
        self.assertEqual(expected, actual)

        expected = ["Republican", "Republican"]
        actual = self.locality_result_service.get_winning_party_history_for_locality("County 3,MO")
        self.assertEqual(expected, actual)

    def test_get_winning_candidate_history_for_locality(self):
        expected = ["Fake Candidate 2", "Fake Candidate 1"]
        actual = self.locality_result_service.get_winning_candidate_history_for_locality("County 1,MO")
        self.assertEqual(expected, actual)

        expected = ["Fake Candidate 1", "Fake Candidate 2"]
        actual = self.locality_result_service.get_winning_candidate_history_for_locality("County 2,MO")
        self.assertEqual(expected, actual)

        expected = ["Fake Candidate 3", "Fake Candidate 2"]
        actual = self.locality_result_service.get_winning_candidate_history_for_locality("County 3,MO")
        self.assertEqual(expected, actual)

    def test_get_counties_for_state(self):
        expected = ["County 1", "County 2", "County 3"]
        actual = self.locality_result_service.get_counties_for_state("MO")
        self.assertEqual(expected, actual)

        expected = ["County 1", "County 2", "County 3"]
        actual = self.locality_result_service.get_counties_for_state("FK")
        self.assertEqual(expected, actual)

    def test_get_localities(self):
        expected = ["County 1,FK", "County 1,MO", "County 2,FK", "County 2,MO", "County 3,FK", "County 3,MO"]
        actual = self.locality_result_service.get_localities()
        self.assertEqual(expected, actual)