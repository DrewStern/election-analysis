import unittest
from unittest import mock

from src.election_result import ElectionResult
from src.election_result_repository import ElectionResultRepository
from src.election_result_service import ElectionResultService


class ElectionResultServiceTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.mock_election_results = [
            ElectionResult(["1993", "MO", "Fake Candidate 1", "Fake Party 1", "120", "21000000", "County 1"]),
            ElectionResult(["1993", "MO", "Fake Candidate 2", "Fake Party 2", "6900", "21000000", "County 1"]),

            ElectionResult(["1993", "MO", "Fake Candidate 1", "Fake Party 1", "451", "21000000", "County 2"]),
            ElectionResult(["1993", "MO", "Fake Candidate 2", "Fake Party 2", "6900", "21000000", "County 2"]),

            ElectionResult(["1993", "MO", "Fake Candidate 1", "Fake Party 1", "451", "21000000", "County 3"]),
            ElectionResult(["1993", "MO", "Fake Candidate 2", "Fake Party 2", "6900", "21000000", "County 3"]),

            ElectionResult(["1997", "FK", "Fake Candidate 1", "Fake Party 1", "121111", "22000000", "County 1"]),
            ElectionResult(["1997", "FK", "Fake Candidate 2", "Fake Party 2", "1901", "22000000", "County 1"]),

            ElectionResult(["1997", "FK", "Fake Candidate 1", "Fake Party 1", "9901", "22000000", "County 2"]),
            ElectionResult(["1997", "FK", "Fake Candidate 2", "Fake Party 2", "12321", "22000000", "County 2"]),

            ElectionResult(["1997", "FK", "Fake Candidate 1", "Fake Party 1", "421", "22000000", "County 3"]),
            ElectionResult(["1997", "FK", "Fake Candidate 2", "Fake Party 2", "6901", "22000000", "County 3"]),

            ElectionResult(["2001", "MO", "Fake Candidate 1", "Fake Party 1", "120", "21000000", "County 1"]),
            ElectionResult(["2001", "MO", "Fake Candidate 2", "Fake Party 2", "6900", "21000000", "County 1"]),

            ElectionResult(["2001", "MO", "Fake Candidate 1", "Fake Party 1", "451", "21000000", "County 2"]),
            ElectionResult(["2001", "MO", "Fake Candidate 2", "Fake Party 2", "6900", "21000000", "County 2"]),

            ElectionResult(["2001", "MO", "Fake Candidate 1", "Fake Party 1", "451", "21000000", "County 3"]),
            ElectionResult(["2001", "MO", "Fake Candidate 2", "Fake Party 2", "6900", "21000000", "County 3"]),

            ElectionResult(["2005", "FK", "Fake Candidate 1", "Fake Party 1", "121111", "22000000", "County 1"]),
            ElectionResult(["2005", "FK", "Fake Candidate 2", "Fake Party 2", "1901", "22000000", "County 1"]),

            ElectionResult(["2005", "FK", "Fake Candidate 1", "Fake Party 1", "9901", "22000000", "County 2"]),
            ElectionResult(["2005", "FK", "Fake Candidate 2", "Fake Party 2", "12321", "22000000", "County 2"]),

            ElectionResult(["2005", "FK", "Fake Candidate 1", "Fake Party 1", "421", "22000000", "County 3"]),
            ElectionResult(["2005", "FK", "Fake Candidate 2", "Fake Party 2", "6901", "22000000", "County 3"]),
        ]

        self.mock_election_result_repository = ElectionResultRepository()
        self.mock_election_result_service = ElectionResultService(self.mock_election_result_repository)
        self.mock_election_result_service.get_election_results = mock.MagicMock(return_value=self.mock_election_results)

    def test_get_election_winner(self):
        expected = "Fake Candidate 2"
        actual = self.mock_election_result_service.get_election_winner("1993", "County 3", "MO")
        self.assertEqual(expected, actual)

        expected = "Fake Candidate 1"
        actual = self.mock_election_result_service.get_election_winner("1997", "County 1", "FK")
        self.assertEqual(expected, actual)

        expected = "Fake Candidate 2"
        actual = self.mock_election_result_service.get_election_winner("2001", "County 2", "MO")
        self.assertEqual(expected, actual)

        expected = "Fake Candidate 2"
        actual = self.mock_election_result_service.get_election_winner("2005", "County 3", "FK")
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
