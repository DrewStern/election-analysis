class MitIntegrationByCandidateTestCases(unittest.TestCase):
    def setUp(self) -> None:
        data_path = self.read_presidential_votes_county_data()
        self.election_result_repository = ElectionResultRepository(data_path)
        self.election_result_service = ElectionResultService(self.election_result_repository)
        self.benford_service = BenfordAnalysisService(self.election_result_service)

    def test_calculate_benford_distribution_by_candidate_AlGore(self):
        expected_distribution = [0, 28.62, 19.32, 12.66, 11.01, 8.15, 6.35, 4.89, 5.46, 3.55]
        actual_distribution = self.benford_service.calculate_benford_distribution(
            self.election_result_service.get_election_results(candidate_filter="Al Gore"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 4.92, 9.77, 1.28, 13.51, 3.16, 5.22, 15.69, 7.06, 22.83]
        actual_deviations = self.benford_service.calculate_deviation_from_benford_distribution(
            actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 22.83
        actual_max_dev = self.benford_service.get_maximum_deviation_from_benford_distribution(
            actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)

    def test_calculate_benford_distribution_by_candidate_GeorgeWBush(self):
        expected_distribution = [0, 28.48, 17.36, 13.72, 10.18, 8.25, 6.96, 5.77, 4.93, 4.35]
        actual_distribution = self.benford_service.calculate_benford_distribution(
            self.election_result_service.get_election_results(candidate_filter="George W. Bush"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 5.38, 1.36, 9.76, 4.95, 4.43, 3.88, 0.52, 3.33, 5.43]
        actual_deviations = self.benford_service.calculate_deviation_from_benford_distribution(
            actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 9.76
        actual_max_dev = self.benford_service.get_maximum_deviation_from_benford_distribution(
            actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)

    def test_calculate_benford_distribution_by_candidate_JohnKerry(self):
        expected_distribution = [0, 28.38, 18.83, 12.71, 10.81, 8.85, 6.66, 4.85, 4.63, 4.28]
        actual_distribution = self.benford_service.calculate_benford_distribution(
            self.election_result_service.get_election_results(candidate_filter="John Kerry"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 5.71, 6.99, 1.68, 11.44, 12.03, 0.6, 16.38, 9.22, 6.96]
        actual_deviations = self.benford_service.calculate_deviation_from_benford_distribution(
            actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 16.38
        actual_max_dev = self.benford_service.get_maximum_deviation_from_benford_distribution(
            actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)

    def test_calculate_benford_distribution_by_candidate_BarackObama(self):
        expected_distribution = [0, 28.64, 18.87, 13.2, 10.19, 7.77, 6.45, 5.55, 4.5, 4.83]
        actual_distribution = self.benford_service.calculate_benford_distribution(
            self.election_result_service.get_election_results(candidate_filter="Barack Obama"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 4.85, 7.22, 5.6, 5.05, 1.65, 3.73, 4.31, 11.76, 5.0]
        actual_deviations = self.benford_service.calculate_deviation_from_benford_distribution(
            actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 11.76
        actual_max_dev = self.benford_service.get_maximum_deviation_from_benford_distribution(
            actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)

    def test_calculate_benford_distribution_by_candidate_JohnMcCain(self):
        expected_distribution = [0, 28.47, 16.84, 12.78, 10.59, 8.85, 6.82, 5.74, 5.36, 4.57]
        actual_distribution = self.benford_service.calculate_benford_distribution(
            self.election_result_service.get_election_results(candidate_filter="John McCain"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 5.42, 4.32, 2.24, 9.18, 12.03, 1.79, 1.03, 5.1, 0.65]
        actual_deviations = self.benford_service.calculate_deviation_from_benford_distribution(
            actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 12.03
        actual_max_dev = self.benford_service.get_maximum_deviation_from_benford_distribution(
            actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)

    def test_calculate_benford_distribution_by_candidate_MittRomney(self):
        expected_distribution = [0, 28.83, 16.48, 12.77, 10.74, 8.78, 7.13, 5.61, 5.45, 4.21]
        actual_distribution = self.benford_service.calculate_benford_distribution(
            self.election_result_service.get_election_results(candidate_filter="Mitt Romney"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 4.22, 6.36, 2.16, 10.72, 11.14, 6.42, 3.28, 6.86, 8.48]
        actual_deviations = self.benford_service.calculate_deviation_from_benford_distribution(
            actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 11.14
        actual_max_dev = self.benford_service.get_maximum_deviation_from_benford_distribution(
            actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)

    def test_calculate_benford_distribution_by_candidate_HillaryClinton(self):
        expected_distribution = [0, 29.91, 18.31, 13.62, 9.57, 6.91, 6.34, 6.4, 4.47, 4.47]
        actual_distribution = self.benford_service.calculate_benford_distribution(
            self.election_result_service.get_election_results(candidate_filter="Hillary Clinton"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 0.63, 4.03, 8.96, 1.34, 12.53, 5.37, 10.34, 12.35, 2.83]
        actual_deviations = self.benford_service.calculate_deviation_from_benford_distribution(
            actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 12.53
        actual_max_dev = self.benford_service.get_maximum_deviation_from_benford_distribution(
            actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)

    def test_calculate_benford_distribution_by_candidate_DonaldTrump_2016(self):
        expected_distribution = [0, 29.44, 16.03, 12.36, 10.23, 9.19, 6.88, 5.93, 5.54, 4.4]
        actual_distribution = self.benford_service.calculate_benford_distribution(
            self.election_result_service.get_election_results(candidate_filter="Donald Trump"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 2.19, 8.92, 1.12, 5.46, 16.33, 2.69, 2.24, 8.63, 4.35]
        actual_deviations = self.benford_service.calculate_deviation_from_benford_distribution(
            actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 16.33
        actual_max_dev = self.benford_service.get_maximum_deviation_from_benford_distribution(
            actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)

    def test_calculate_benford_distribution_by_candidate_DonaldTrump_2020(self):
        expected_distribution = [3.79, 29.49, 17.31, 11.2, 9.11, 7.7, 6.23, 5.41, 5.02, 4.73]
        actual_distribution = self.benford_service.calculate_benford_distribution(
            self.election_result_service.get_election_results(candidate_filter="Donald J Trump"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 2.03, 1.65, 10.4, 6.08, 2.53, 7.01, 6.72, 1.57, 2.83]
        actual_deviations = self.benford_service.calculate_deviation_from_benford_distribution(
            actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 10.4
        actual_max_dev = self.benford_service.get_maximum_deviation_from_benford_distribution(
            actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)

    def test_calculate_benford_distribution_by_candidate_JoeBiden(self):
        expected_distribution = [4.33, 28.55, 17.11, 12.25, 9.99, 7.17, 6.07, 5.15, 4.98, 4.39]
        actual_distribution = self.benford_service.calculate_benford_distribution(
            self.election_result_service.get_election_results(candidate_filter="Joseph R Biden Jr"))
        self.assertEqual(expected_distribution, actual_distribution)
        expected_deviations = ["INF", 5.15, 2.78, 2.0, 2.99, 9.24, 9.4, 11.21, 2.35, 4.57]
        actual_deviations = self.benford_service.calculate_deviation_from_benford_distribution(
            actual_distribution)
        self.assertEqual(expected_deviations, actual_deviations)
        expected_max_dev = 11.21
        actual_max_dev = self.benford_service.get_maximum_deviation_from_benford_distribution(
            actual_distribution)
        self.assertEqual(expected_max_dev, actual_max_dev)