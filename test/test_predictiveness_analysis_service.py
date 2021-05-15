import unittest
from unittest import mock

from src.election_result import ElectionResult
from src.election_result_repository import ElectionResultRepository
from src.predictiveness_analysis_service import PredictivenessAnalysisService


class PredictivenessAnalysisServiceTestCase(unittest.TestCase):
    def setUp(self):
        self.mock_election_result_data = [
            ElectionResult(["1993", "MO", "Fake Candidate 1", "Fake Party 1", "120", "21000000", "MO County 1"]),
            ElectionResult(["1993", "MO", "Fake Candidate 1", "Fake Party 1", "451", "21000000", "MO County 2"]),
            ElectionResult(["1993", "MO", "Fake Candidate 1", "Fake Party 1", "451", "21000000", "MO County 3"]),
            ElectionResult(["1993", "MO", "Fake Candidate 2", "Fake Party 2", "6900", "21000000", "MO County 1"]),
            ElectionResult(["1993", "MO", "Fake Candidate 2", "Fake Party 2", "6900", "21000000", "MO County 2"]),
            ElectionResult(["1993", "MO", "Fake Candidate 2", "Fake Party 2", "6900", "21000000", "MO County 3"]),
            ElectionResult(["1993", "MO", "Fake Candidate 3", "Fake Party 3", "8100", "21000000", "MO County 1"]),
            ElectionResult(["1993", "MO", "Fake Candidate 3", "Fake Party 3", "8100", "21000000", "MO County 2"]),
            ElectionResult(["1993", "MO", "Fake Candidate 3", "Fake Party 3", "1100", "21000000", "MO County 3"]),

            ElectionResult(["1996", "FK", "Fake Candidate 1", "Fake Party 1", "121", "22000000", "Fake County 1"]),
            ElectionResult(["1996", "FK", "Fake Candidate 1", "Fake Party 1", "12321", "22000000", "Fake County 2"]),
            ElectionResult(["1996", "FK", "Fake Candidate 1", "Fake Party 1", "421", "22000000", "Fake County 3"]),
            ElectionResult(["1996", "FK", "Fake Candidate 2", "Fake Party 2", "1901", "22000000", "Fake County 1"]),
            ElectionResult(["1996", "FK", "Fake Candidate 2", "Fake Party 2", "9901", "22000000", "Fake County 2"]),
            ElectionResult(["1996", "FK", "Fake Candidate 2", "Fake Party 2", "6901", "22000000", "Fake County 3"]),
            ElectionResult(["1996", "FK", "Fake Candidate 3", "Fake Party 3", "8101", "22000000", "Fake County 1"]),
            ElectionResult(["1996", "FK", "Fake Candidate 3", "Fake Party 3", "1101", "22000000", "Fake County 2"]),
            ElectionResult(["1996", "FK", "Fake Candidate 3", "Fake Party 3", "8101", "22000000", "Fake County 3"]),
        ]

        self.mock_election_result_repository = ElectionResultRepository()
        self.mock_election_result_repository.get_election_results = mock.MagicMock(self.mock_election_result_data)

        self.mock_election_predictiveness_analysis_service = PredictivenessAnalysisService(
            self.mock_election_result_repository)

if __name__ == '__main__':
    unittest.main()
