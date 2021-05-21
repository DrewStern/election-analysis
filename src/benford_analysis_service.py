class BenfordAnalysisService:
    def calculate_benford_distribution(self, election_results):
        leading_digit_occurrences = 9 * [0]
        for election_result in election_results:
            leading_digit = int(election_result.candidatevotes[0])
            leading_digit_occurrences[leading_digit - 1] += 1
        return [round(100 * int(x) / int(sum(leading_digit_occurrences)), 2) for x in leading_digit_occurrences]