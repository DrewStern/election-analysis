class PredictivenessAnalysisService:
    def __init__(self, election_result_repository):
        self.election_result_repository = election_result_repository

    def find_counties_predictive_of_winner(self, prediction_rate_by_county):
        return [county for county in prediction_rate_by_county if prediction_rate_by_county[county] == 1]

    def find_counties_predictive_of_loser(self, prediction_rate_by_county):
        return [county for county in prediction_rate_by_county if prediction_rate_by_county[county] == 0]

    def get_prediction_rate_by_county(self, election_results):
        correct_predictions = dict()
        for election_result in election_results:
            if correct_predictions.get(election_result.locale) is None:
                correct_predictions[election_result.locale] = 0
            if self.was_prediction_correct(election_result):
                correct_predictions[election_result.locale] += 1
        number_of_elections = self.get_number_of_elections(election_results)
        return {county: correct_predictions / number_of_elections for county, correct_predictions in correct_predictions.items()}

    def get_number_of_elections(self, election_results):
        election_years = []
        for election_result in election_results:
            if election_result.year not in election_years:
                election_years.append(election_result.year)
        return len(election_years)

    def get_election_winner(self, election_results, year, county, state):
        locale_election_candidate_results = []
        for election_result in election_results:
            if election_result.is_from_election(year, county, state):
                locale_election_candidate_results.append(election_result)
        return sorted(locale_election_candidate_results, key=lambda x: int(x.candidatevotes), reverse=True)[0].candidate

    def was_prediction_correct(self, election_result):
        nationally_winning_candidates_by_year = self.election_result_repository.get_nationally_winning_candidates_by_year()
        return nationally_winning_candidates_by_year[election_result.year] == election_result.candidate
