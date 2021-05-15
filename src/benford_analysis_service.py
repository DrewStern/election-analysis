class BenfordAnalysisService:
    def calculate_benford_distribution(self, raw_vote_data):
        leading_digit_occurrences = 9 * [0]
        for election_result in raw_vote_data:
            leading_digit = int(election_result.candidatevotes[0])
            leading_digit_occurrences[leading_digit - 1] += 1
        return [round(100 * int(x) / int(sum(leading_digit_occurrences)), 2) for x in leading_digit_occurrences]