class BenfordAnalysisService:
    def __init__(self, election_result_repository):
        self.election_result_repository = election_result_repository

    def calculate_benford_distributions_new(self, raw_vote_data):
        pass

    def calculate_leading_digit_proportions_new(self, raw_vote_distribution):
        sum_of_all_leading_digit_counts = sum(raw_vote_distribution)
        # return [100 * int(x) / int(sum_of_all_leading_digit_counts) for x in raw_vote_distribution]
        return [100 * int(x.candidatevotes) / sum_of_all_leading_digit_counts for x in raw_vote_distribution]

    def sum_votes_by_leading_digit_new(self, raw_vote_data):
        raw_vote_distribution = 9 * [0]
        for election_result in raw_vote_data:
            leading_digit = int(election_result.candidatevotes[0])
            raw_vote_distribution[leading_digit - 1] += 1
        return raw_vote_distribution

    def calculate_benford_distributions_old(self, raw_vote_data):
        return self.calculate_leading_digit_proportions_old(self.sum_votes_by_leading_digit_old(raw_vote_data))

    def calculate_leading_digit_proportions_old(self, raw_vote_distribution):
        benford_distribution = dict()
        for year in raw_vote_distribution.keys():
            benford_distribution[year] = dict()
            for candidate in raw_vote_distribution[year].keys():
                sum_of_all_leading_digit_counts = sum(raw_vote_distribution[year][candidate])
                benford_distribution[year][candidate] = [100 * int(x) / int(sum_of_all_leading_digit_counts) for x in
                                                         raw_vote_distribution[year][candidate]]
        return benford_distribution

    def sum_votes_by_leading_digit_old(self, raw_vote_data):
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
