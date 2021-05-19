class PredictivenessAnalysisService:
    def __init__(self, election_result_repository):
        self.election_result_repository = election_result_repository

    def find_counties_predictive_of_winner(self, prediction_rate_by_county):
        return [county for county in prediction_rate_by_county if prediction_rate_by_county[county] == 1]

    def find_counties_predictive_of_loser(self, prediction_rate_by_county):
        return [county for county in prediction_rate_by_county if prediction_rate_by_county[county] == 0]

    def get_prediction_rate_by_county(self, raw_vote_data):
        prediction_rate_by_county = dict()
        election_years = []

        for vote_data in raw_vote_data:
            if vote_data.year not in election_years:
                election_years.append(vote_data.year)
            if prediction_rate_by_county.get(vote_data.locale) is None:
                prediction_rate_by_county[vote_data.locale] = 0
            if self.was_prediction_correct(vote_data):
                prediction_rate_by_county[vote_data.locale] += 1

        number_of_elections = len(election_years)
        for county in prediction_rate_by_county:
            prediction_rate_by_county[county] = prediction_rate_by_county[county] / number_of_elections

        return prediction_rate_by_county

    def get_locale_election_winner_by_year(self, election_results, year, county, state):
        locale_election_candidate_results = []
        for election_result in election_results:
            if election_result.is_from_same_election(year, county, state):
                locale_election_candidate_results.append(election_result)
        # need to cast to int so that sort works correctly
        # e.g., so that 1901 > 12111 as expected; otherwise sort orders "12111" > "1901"
        return sorted(locale_election_candidate_results, key=lambda x: int(x.candidatevotes), reverse=True)[0].candidate

    def was_prediction_correct(self, vote_data):
        nationally_winning_candidates_by_year = self.election_result_repository.get_nationally_winning_candidates_by_year()
        return nationally_winning_candidates_by_year[vote_data.year] == vote_data.candidate
