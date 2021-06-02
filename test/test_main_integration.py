import unittest

from src.main import read_presidential_votes_county_data
from src.repositories.election_result_repository import ElectionResultRepository
from src.services.benford_analysis_service import BenfordAnalysisService
from src.services.election_result_service import ElectionResultService


class MainIntegrationTestCases(unittest.TestCase):
    def setUp(self) -> None:
        self.election_result_repository = ElectionResultRepository(read_presidential_votes_county_data())
        self.election_result_service = ElectionResultService(self.election_result_repository)
        county_level_results = self.election_result_service.get_election_results()

        self.benford_analysis_service = BenfordAnalysisService(self.election_result_service)

    def test_overall_benford_distribution(self):
        # for now this is just a copy/paste of the output, need to double check vs expected distribution +/- some tolerances
        expected = [28.79, 17.83, 13.07, 10.37, 8.27, 6.7, 5.6, 4.98, 4.38]
        actual = self.benford_analysis_service.calculate_benford_distribution()
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
