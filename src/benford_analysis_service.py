class BenfordAnalysisService:
    def calculate_benford_distributions(self, raw_vote_data):
        return self.calculate_leading_digit_proportions(self.sum_votes_by_leading_digit(raw_vote_data))

    def calculate_leading_digit_proportions(self, raw_vote_distribution):
        benford_distribution = dict()
        for year in raw_vote_distribution.keys():
            benford_distribution[year] = dict()
            for candidate in raw_vote_distribution[year].keys():
                sum_of_all_leading_digit_counts = sum(raw_vote_distribution[year][candidate])
                benford_distribution[year][candidate] = [100 * int(x) / int(sum_of_all_leading_digit_counts) for x in
                                                         raw_vote_distribution[year][candidate]]
        return benford_distribution

    def sum_votes_by_leading_digit(self, raw_vote_data):
        # basic structure of the data is nested dictionary: <year, <candidate, [benford_distribution]>>
        raw_vote_distribution = dict()
        for election_result in raw_vote_data:
            if not raw_vote_distribution.get(election_result.year):
                raw_vote_distribution[election_result.year] = dict()

            if not raw_vote_distribution.get(election_result.year).get(election_result.candidate):
                raw_vote_distribution[election_result.year][election_result.candidate] = 9 * [0]

            leading_digit = int(election_result.candidatevotes[0])
            raw_vote_distribution[election_result.year][election_result.candidate][leading_digit - 1] += 1
        return raw_vote_distribution

    def write_benford_distributions(self, benford_distributions, output_path):
        with open(output_path, 'w') as csvfile:
            csvfile.write("YEAR,CANDIDATE,ONES,TWOS,THREES,FOURS,FIVES,SIXES,SEVENS,EIGHTS,NINES\n")
            for outer_key in benford_distributions:
                candidate_benford_distributions = benford_distributions[outer_key]
                for inner_key in candidate_benford_distributions:
                    benford_distribution = candidate_benford_distributions[inner_key]
                    csvfile.write(outer_key + ",'" + inner_key + "'," + ",".join(map(str, benford_distribution)) + "\n")
            csvfile.close()