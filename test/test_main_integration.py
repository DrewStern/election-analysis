import unittest

from src.main import read_presidential_votes_county_data
from src.repositories.election_result_repository import ElectionResultRepository
from src.services.benford_analysis_service import BenfordAnalysisService
from src.services.election_result_service import ElectionResultService


class MainIntegrationTestCases(unittest.TestCase):
    def setUp(self) -> None:
        self.election_result_repository = ElectionResultRepository(read_presidential_votes_county_data())
        self.election_result_service = ElectionResultService(self.election_result_repository)
        self.benford_analysis_service = BenfordAnalysisService(self.election_result_service)

    # for now this is just a copy/paste of the output, need to double check vs expected distribution +/- some tolerances
    def test_calculate_benford_distribution(self):
        expected = [28.79, 17.83, 13.07, 10.37, 8.27, 6.7, 5.6, 4.98, 4.38]
        actual = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results())
        self.assertEqual(expected, actual)

        expected = [29.44, 16.03, 12.36, 10.23, 9.19, 6.88, 5.93, 5.54, 4.4]
        actual = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(candidate_filter="Donald Trump"))
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
