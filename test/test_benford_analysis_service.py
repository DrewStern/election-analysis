import unittest

from src.services.benford_analysis_service import BenfordAnalysisService
from src.services.election_result_service import ElectionResultService
from src.repositories.mock_election_result_repository import MockElectionResultRepository


class BenfordAnalysisServiceTestCase(unittest.TestCase):
    def setUp(self):
        self.mock_election_result_service = ElectionResultService(MockElectionResultRepository())
        self.benford_analysis_service = BenfordAnalysisService(self.mock_election_result_service)

    def test_calculate_benford_distribution(self):
        expected = [32, 0, 0, 24, 0, 32, 4, 0, 8]
        actual = self.benford_analysis_service.calculate_benford_distribution(self.mock_election_result_service.get_election_results())
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
