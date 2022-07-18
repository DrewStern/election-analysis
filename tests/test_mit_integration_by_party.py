class MitIntegrationByPartyTestCases(unittest.TestCase):
    def setUp(self) -> None:
        data_path = self.read_presidential_votes_county_data()
        self.election_result_repository = ElectionResultRepository(data_path)
        self.election_result_service = ElectionResultService(self.election_result_repository)
        self.benford_service = BenfordAnalysisService(self.election_result_service)

    def test_calculate_benford_distribution_by_party_Democrat(self):
        expected_distribution = [1.06, 28.77, 18.42, 12.88, 10.27, 7.71, 6.36, 5.37, 4.78, 4.39]
        actual_distribution = self.benford_service.calculate_benford_distribution(
            self.election_result_service.get_election_results(party_filter="Democrat"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 4.42, 4.66, 3.04, 5.88, 2.41, 5.07, 7.41, 6.27, 4.57]
        actual_deviations = self.benford_service.calculate_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 7.41
        actual_max_dev = self.benford_service.get_maximum_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)


    def test_calculate_benford_distribution_by_party_Republican(self):
        expected_distribution = [0.93, 28.92, 16.94, 12.61, 10.07, 8.43, 6.77, 5.68, 5.19, 4.46]
        actual_distribution = self.benford_service.calculate_benford_distribution(
            self.election_result_service.get_election_results(party_filter="Republican"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 3.92, 3.75, 0.88, 3.81, 6.71, 1.04, 2.07, 1.76, 3.04]
        actual_deviations = self.benford_service.calculate_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 6.71
        actual_max_dev = self.benford_service.get_maximum_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)