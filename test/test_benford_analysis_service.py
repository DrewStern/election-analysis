import unittest

from src.services.benford_analysis_service import BenfordAnalysisService
from src.services.election_result_service import ElectionResultService
from src.repositories.mock_election_result_repository import MockElectionResultRepository


class BenfordAnalysisServiceTestCase(unittest.TestCase):
    def setUp(self):
        self.benford_analysis_service = BenfordAnalysisService(ElectionResultService(MockElectionResultRepository()))

    def test_calculate_benford_distribution(self):
        expected = [32, 0, 0, 24, 0, 32, 4, 0, 8]
        actual = self.benford_analysis_service.calculate_benford_distribution()
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
