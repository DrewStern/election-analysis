import unittest

from src.data.models.election_event import ElectionEvent
from src.data.repositories.mock_election_result_repository import MockElectionResultRepository
from src.services.election_result_service import ElectionResultService
from src.services.election_event_service import ElectionEventService


class ElectionEventServiceTestCases(unittest.TestCase):
    def setUp(self) -> None:
        self.mock_election_result_repository = MockElectionResultRepository()
        self.election_result_service = ElectionResultService(self.mock_election_result_repository)
        self.election_event_service = ElectionEventService(self.election_result_service)

    def test_get_election_years(self):
        expected = ["1993", "1997", "2001", "2005"]
        actual = self.election_event_service.get_election_years()
        self.assertEqual(expected, actual)

    def test_get_election_events(self):
        expected = [
            ElectionEvent("1993", "MO", "County 1"),
            ElectionEvent("1993", "MO", "County 2"),
            ElectionEvent("1993", "MO", "County 3"),
            ElectionEvent("1997", "FK", "County 1"),
            ElectionEvent("1997", "FK", "County 2"),
            ElectionEvent("1997", "FK", "County 3"),
            ElectionEvent("2001", "MO", "County 1"),
            ElectionEvent("2001", "MO", "County 2"),
            ElectionEvent("2001", "MO", "County 3"),
            ElectionEvent("2005", "FK", "County 1"),
            ElectionEvent("2005", "FK", "County 2"),
            ElectionEvent("2005", "FK", "County 3"),
        ]
        actual = self.election_event_service.get_election_events()
        self.assertEqual(expected, actual)

    def test_get_counties_won_by_party(self):
        expected = ["County 1", "County 3"]
        actual = self.election_event_service.get_counties_won_by_party("1993", "MO", "Republican")
        self.assertEqual(expected, actual)

        expected = ["County 2"]
        actual = self.election_event_service.get_counties_won_by_party("1993", "MO", "Democrat")
        self.assertEqual(expected, actual)

        expected = ["County 2", "County 3"]
        actual = self.election_event_service.get_counties_won_by_party("1997", "FK", "Republican")
        self.assertEqual(expected, actual)

        expected = ["County 1"]
        actual = self.election_event_service.get_counties_won_by_party("1997", "FK", "Democrat")
        self.assertEqual(expected, actual)

        expected = ["County 2", "County 3"]
        actual = self.election_event_service.get_counties_won_by_party("2001", "MO", "Republican")
        self.assertEqual(expected, actual)

        expected = ["County 1"]
        actual = self.election_event_service.get_counties_won_by_party("2001", "MO", "Democrat")
        self.assertEqual(expected, actual)

        expected = ["County 2"]
        actual = self.election_event_service.get_counties_won_by_party("2005", "FK", "Republican")
        self.assertEqual(expected, actual)

        expected = ["County 1", "County 3"]
        actual = self.election_event_service.get_counties_won_by_party("2005", "FK", "Democrat")
        self.assertEqual(expected, actual)

    def test_get_counties_for_state(self):
        expected = ["County 1", "County 2", "County 3"]
        actual = self.election_event_service.get_counties_for_state("MO")
        self.assertEqual(expected, actual)

        expected = ["County 1", "County 2", "County 3"]
        actual = self.election_event_service.get_counties_for_state("FK")
        self.assertEqual(expected, actual)

    def test_get_localities(self):
        expected = ["County 1,FK", "County 1,MO", "County 2,FK", "County 2,MO", "County 3,FK", "County 3,MO"]
        actual = self.election_event_service.get_localities()
        self.assertEqual(expected, actual)