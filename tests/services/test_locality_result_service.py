import unittest

from src.repositories.mock_election_result_repository import MockElectionResultRepository
from src.services.election_result_service import ElectionResultService
from src.services.locality_result_service import LocalityResultService


class LocalityResultServiceTestCases(unittest.TestCase):
    def setUp(self) -> None:
        self.mock_election_result_repository = MockElectionResultRepository()
        self.election_result_service = ElectionResultService(self.mock_election_result_repository)
        self.locality_result_service = LocalityResultService(self.election_result_service)

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
