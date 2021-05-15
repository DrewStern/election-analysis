class BenfordAnalysisService:
    def __init__(self, election_result_repository):
        self.election_result_repository = election_result_repository

    def calculate_benford_distributions_new(self, raw_vote_data):
        pass

    def calculate_leading_digit_proportions_new(self, leading_digit_occurrences):
        sum_of_all_leading_digit_counts = sum(leading_digit_occurrences)
        return [100 * int(x) / int(sum_of_all_leading_digit_counts) for x in leading_digit_occurrences]

    def sum_votes_by_leading_digit_new(self, raw_vote_data):
        leading_digit_occurrences = 9 * [0]
        for election_result in raw_vote_data:
            leading_digit = int(election_result.candidatevotes[0])
            leading_digit_occurrences[leading_digit - 1] += 1
        return leading_digit_occurrences

    def calculate_benford_distributions_old(self, raw_vote_data):
        return self.calculate_leading_digit_proportions_old(self.sum_votes_by_leading_digit_old(raw_vote_data))

    def calculate_leading_digit_proportions_old(self, leading_digit_occurrences):
        benford_distribution = dict()
        for year in leading_digit_occurrences.keys():
            benford_distribution[year] = dict()
            for candidate in leading_digit_occurrences[year].keys():
                sum_of_all_leading_digit_counts = sum(leading_digit_occurrences[year][candidate])
                benford_distribution[year][candidate] = [100 * int(x) / int(sum_of_all_leading_digit_counts) for x in
                                                         leading_digit_occurrences[year][candidate]]
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
