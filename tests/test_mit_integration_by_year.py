class MitIntegrationByYearTestCases(unittest.TestCase):
    def setUp(self) -> None:
        data_path = self.read_presidential_votes_county_data()
        self.election_result_repository = ElectionResultRepository(data_path)
        self.election_result_service = ElectionResultService(self.election_result_repository)
        self.benford_analysis_service = BenfordAnalysisService(self.election_result_service)

    def test_calculate_benford_distribution_by_year_2000(self):
        expected_distribution = [0, 28.39, 18.69, 13.44, 10.63, 8.04, 6.76, 4.93, 5.2, 3.92]
        actual_distribution = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(year_filter="2000"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 5.68, 6.19, 7.52, 9.59, 1.77, 0.9, 15.0, 1.96, 14.78]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 15.0
        actual_max_dev = self.benford_analysis_service.get_maximum_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)

    def test_calculate_benford_distribution_by_year_2004(self):
        expected_distribution = [0, 28.58, 17.76, 12.97, 10.46, 8.7, 6.71, 5.71, 4.77, 4.34]
        actual_distribution = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(year_filter="2004"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 5.05, 0.91, 3.76, 7.84, 10.13, 0.15, 1.55, 6.47, 5.65]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 10.13
        actual_max_dev = self.benford_analysis_service.get_maximum_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)

    def test_calculate_benford_distribution_by_year_2008(self):
        expected_distribution = [0, 28.46, 17.8, 13.02, 10.56, 8.32, 6.67, 5.88, 4.85, 4.44]
        actual_distribution = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(year_filter="2008"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 5.45, 1.14, 4.16, 8.87, 5.32, 0.45, 1.38, 4.9, 3.48]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 8.87
        actual_max_dev = self.benford_analysis_service.get_maximum_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)

    def test_calculate_benford_distribution_by_year_2012(self):
        expected_distribution = [0, 28.83, 17.73, 12.96, 10.3, 8.25, 6.75, 5.34, 5.05, 4.78]
        actual_distribution = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(year_filter="2012"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 4.22, 0.74, 3.68, 6.19, 4.43, 0.75, 7.93, 0.98, 3.91]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 7.93
        actual_max_dev = self.benford_analysis_service.get_maximum_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)

    def test_calculate_benford_distribution_by_year_2016(self):
        expected_distribution = [0, 29.67, 17.17, 12.99, 9.9, 8.05, 6.61, 6.16, 5.01, 4.44]
        actual_distribution = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(year_filter="2016"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 1.43, 2.44, 3.92, 2.06, 1.9, 1.34, 6.21, 1.76, 3.48]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 6.21
        actual_max_dev = self.benford_analysis_service.get_maximum_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)

    def test_calculate_benford_distribution_by_year_2020(self):
        expected_distribution = [4.06, 29.02, 17.21, 11.72, 9.55, 7.44, 6.15, 5.28, 5.0, 4.56]
        actual_distribution = self.benford_analysis_service.calculate_benford_distribution(self.election_result_service.get_election_results(year_filter="2020"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 3.59, 2.22, 6.24, 1.55, 5.82, 8.21, 8.97, 1.96, 0.87]
        actual_deviations = self.benford_analysis_service.calculate_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 8.97
        actual_max_dev = self.benford_analysis_service.get_maximum_deviation_from_benford_distribution(actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)