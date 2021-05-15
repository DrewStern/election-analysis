class PredictivenessAnalysisService:
    def __init__(self, election_result_repository):
        self.election_result_repository = election_result_repository

    def find_counties_predictive_of_winner(self, prediction_rate_by_county):
        return [county for county in prediction_rate_by_county if prediction_rate_by_county[county] == 1]

    def find_counties_predictive_of_loser(self, prediction_rate_by_county):
        return [county for county in prediction_rate_by_county if prediction_rate_by_county[county] == 0]

    def get_prediction_rate_by_county(self, candidate_votes_by_year_county):
        number_of_elections = len(candidate_votes_by_year_county.keys())
        prediction_rate_by_county = dict()
        for county_prediction_result in self.get_correct_predictions_by_county(candidate_votes_by_year_county).items():
            prediction_rate_by_county[county_prediction_result[0]] = county_prediction_result[1] / number_of_elections
        return prediction_rate_by_county

    def get_correct_predictions_by_county(self, candidate_votes_by_year_county):
        correct_predictions_by_county = dict()
        for year in candidate_votes_by_year_county:
            for county_prediction_result in candidate_votes_by_year_county[year]:
                county_winner = None
                for candidate_result in candidate_votes_by_year_county[year][county_prediction_result].items():
                    if county_winner is None:
                        county_winner = candidate_result
                    if candidate_result[1] > county_winner[1]:
                        county_winner = candidate_result
                if correct_predictions_by_county.get(county_prediction_result) is None:
                    correct_predictions_by_county[county_prediction_result] = 0
                if county_winner[0] in self.election_result_repository.get_nationally_winning_candidates_by_year().values():
                    correct_predictions_by_county[county_prediction_result] += 1
        return correct_predictions_by_county