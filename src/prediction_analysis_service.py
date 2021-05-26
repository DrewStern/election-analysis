from src.election_result_service import ElectionResultService


class PredictionAnalysisService:
    def __init__(self, election_result_service: ElectionResultService):
        self.election_result_service = election_result_service

    def find_counties_predictive_of_winner(self, prediction_rate_by_county):
        return [county for county in prediction_rate_by_county if prediction_rate_by_county[county] == 1]

    def find_counties_predictive_of_loser(self, prediction_rate_by_county):
        return [county for county in prediction_rate_by_county if prediction_rate_by_county[county] == 0]

    def get_prediction_rate_by_county(self, election_results):
        correct_predictions = self.sum_correct_predictions_by_county(election_results)
        number_of_elections = len(self.election_result_service.get_election_years())
        if number_of_elections == 0:
            raise ZeroDivisionError("number_of_elections found to be zero")
        return {county: correct_predictions / number_of_elections for county, correct_predictions in correct_predictions.items()}

    def sum_correct_predictions_by_county(self, election_results):
        correct_predictions = dict()
        for election_result in election_results:
            if correct_predictions.get(election_result.locale) is None:
                correct_predictions[election_result.locale] = 0
            if self.was_prediction_correct(election_result):
                correct_predictions[election_result.locale] += 1
        return correct_predictions

    def was_prediction_correct(self, election_result):
        nationally_winning_candidate = self.election_result_service.get_nationally_winning_candidate_by_year(election_result.year)
        return nationally_winning_candidate == election_result.candidate
