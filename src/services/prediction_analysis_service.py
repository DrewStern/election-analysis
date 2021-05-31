from src.services.election_result_service import ElectionResultService


class PredictionAnalysisService:
    def __init__(self, election_result_service: ElectionResultService):
        self.election_result_service = election_result_service

    def find_locales_with_prediction_rate_above(self, prediction_rate_by_locale, prediction_rate_lower_cutoff):
        return [locale for locale in prediction_rate_by_locale if prediction_rate_by_locale[locale] >= prediction_rate_lower_cutoff]

    def find_locales_with_prediction_rate_below(self, prediction_rate_by_locale, prediction_rate_upper_cutoff):
        return [locale for locale in prediction_rate_by_locale if prediction_rate_by_locale[locale] <= prediction_rate_upper_cutoff]

    # TODO: in progress
    def get_locale_prediction_ranking(self, election_results):
        prediction_rate_by_locale = self.get_prediction_rate_by_locale(election_results)
        return sorted(prediction_rate_by_locale, key=lambda x: x.values())

    def get_prediction_rate_by_locale(self, election_results):
        correct_predictions = self.sum_correct_predictions_by_locale(election_results)
        number_of_elections = len(self.election_result_service.get_election_years())
        if number_of_elections == 0:
            raise ZeroDivisionError("number_of_elections found to be zero")
        return {locale: correct_predictions / number_of_elections for locale, correct_predictions in correct_predictions.items()}
        # return map(lambda x: x.keys() / number_of_elections, correct_predictions)

    def sum_correct_predictions_by_locale(self, election_results):
        tallied = []
        locale_predictions = self.init_locale_dict(election_results, 0)
        for election_result in election_results:
            county_winner = self.election_result_service.get_election_winner(election_result.year, election_result.county, election_result.state)
            nation_winner = self.election_result_service.get_nationally_winning_candidate_by_year(election_result.year)
            if county_winner == nation_winner and (election_result.year, election_result.county, election_result.state) not in tallied:
                locale_predictions[election_result.locale] += 1
                tallied.append((election_result.year, election_result.county, election_result.state))
        return locale_predictions

    def init_locale_dict(self, election_results, default_value):
        locale_dict = dict()
        for election_result in election_results:
            if locale_dict.get(election_result.locale) is None:
                locale_dict[election_result.locale] = default_value
        return locale_dict
