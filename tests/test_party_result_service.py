import unittest

from src.repositories.mock_election_result_repository import MockElectionResultRepository
from src.services.election_result_service import ElectionResultService
from src.services.locality_result_service import LocalityResultService
from src.services.party_result_service import PartyResultService


class PartyResultServiceTestCases(unittest.TestCase):
    def setUp(self) -> None:
        self.mock_election_result_repository = MockElectionResultRepository()
        self.election_result_service = ElectionResultService(self.mock_election_result_repository)
        self.locality_result_service = LocalityResultService(self.election_result_service)
        self.party_result_service = PartyResultService(self.election_result_service, self.locality_result_service)

    def test_get_counties_won_by_party(self):
        expected = ["County 1", "County 3"]
        actual = self.party_result_service.get_counties_won_by_party("1993", "MO", "Republican")
        self.assertEqual(expected, actual)

        expected = ["County 2"]
        actual = self.party_result_service.get_counties_won_by_party("1993", "MO", "Democrat")
        self.assertEqual(expected, actual)

        expected = ["County 2", "County 3"]
        actual = self.party_result_service.get_counties_won_by_party("1997", "FK", "Republican")
        self.assertEqual(expected, actual)

        expected = ["County 1"]
        actual = self.party_result_service.get_counties_won_by_party("1997", "FK", "Democrat")
        self.assertEqual(expected, actual)

        expected = ["County 2", "County 3"]
        actual = self.party_result_service.get_counties_won_by_party("2001", "MO", "Republican")
        self.assertEqual(expected, actual)

        expected = ["County 1"]
        actual = self.party_result_service.get_counties_won_by_party("2001", "MO", "Democrat")
        self.assertEqual(expected, actual)

        expected = ["County 2"]
        actual = self.party_result_service.get_counties_won_by_party("2005", "FK", "Republican")
        self.assertEqual(expected, actual)

        expected = ["County 1", "County 3"]
        actual = self.party_result_service.get_counties_won_by_party("2005", "FK", "Democrat")
        self.assertEqual(expected, actual)