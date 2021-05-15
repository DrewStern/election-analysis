class BenfordAnalysisService:
    def __init__(self, election_result_repository):
        self.election_result_repository = election_result_repository

    def calculate_benford_distributions(self, raw_vote_data):
        return self.calculate_leading_digit_proportions(self.sum_votes_by_leading_digit(raw_vote_data))

    def calculate_leading_digit_proportions(self, leading_digit_occurrences):
        sum_of_leading_digit_occurrences = sum(leading_digit_occurrences)
        return [100 * int(x) / int(sum_of_leading_digit_occurrences) for x in leading_digit_occurrences]

    def sum_votes_by_leading_digit(self, raw_vote_data):
        leading_digit_occurrences = 9 * [0]
        for election_result in raw_vote_data:
            leading_digit = int(election_result.candidatevotes[0])
            leading_digit_occurrences[leading_digit - 1] += 1
        return leading_digit_occurrences