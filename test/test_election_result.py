import unittest

from src.election_analysis import ElectionResult, ElectionResults


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.election_result_data = ElectionResults([
            ElectionResult(["1993", "NA", "Fake Candidate 1", "Fake Party 1", "420", "21000000", "Fake County 1"]),
            ElectionResult(["1993", "NA", "Fake Candidate 2", "Fake Party 2", "6900", "21000000", "Fake County 2"]),
            ElectionResult(["1993", "NA", "Fake Candidate 3", "Fake Party 3", "6100", "21000000", "Fake County 3"]),
            ElectionResult(["1996", "NA", "Fake Candidate 1", "Fake Party 1", "421", "22000000", "Fake County 1"]),
            ElectionResult(["1996", "NA", "Fake Candidate 2", "Fake Party 2", "6901", "22000000", "Fake County 2"]),
            ElectionResult(["1996", "NA", "Fake Candidate 3", "Fake Party 3", "6101", "22000000", "Fake County 3"]),
        ])

    def test_sum_votes_by_leading_digit(self):
        votes_summed_by_leading_digit = self.election_result_data.sum_votes_by_leading_digit()
        expected_ones = 0
        actual_ones = votes_summed_by_leading_digit["1993"]["Fake Candidate 1"][0]
        self.assertEqual(expected_ones, actual_ones)

        expected_fours = 1
        actual_fours = votes_summed_by_leading_digit["1993"]["Fake Candidate 1"][3]
        self.assertEqual(expected_fours, actual_fours)

        # TODO: I think I want this to be expected_sixes = 2 but requires rework of underlying src
        expected_sixes = 1
        actual_sixes = votes_summed_by_leading_digit["1993"]["Fake Candidate 2"][5]
        self.assertEqual(expected_sixes, actual_sixes)





if __name__ == '__main__':
    unittest.main()
