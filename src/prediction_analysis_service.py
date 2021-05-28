from src.election_result_service import ElectionResultService


class PredictionAnalysisService:
    def __init__(self, election_result_service: ElectionResultService):
        self.election_result_service = election_result_service

    def find_locales_predictive_of_winner(self, prediction_rate_by_locale):
        return [locale for locale in prediction_rate_by_locale if prediction_rate_by_locale[locale] == 1]

    def find_locales_predictive_of_loser(self, prediction_rate_by_locale):
        return [locale for locale in prediction_rate_by_locale if prediction_rate_by_locale[locale] == 0]

    def find_locales_with_prediction_rate_above(self, prediction_rate_by_locale, prediction_rate_lower_cutoff):
        return [locale for locale in prediction_rate_by_locale if prediction_rate_by_locale[locale] > prediction_rate_lower_cutoff]

    def find_locales_with_prediction_rate_below(self, prediction_rate_by_locale, prediction_rate_upper_cutoff):
        return [locale for locale in prediction_rate_by_locale if prediction_rate_by_locale[locale] < prediction_rate_upper_cutoff]

    def get_prediction_rate_by_locale(self, election_results):
        correct_predictions = self.sum_correct_predictions_by_locale(election_results)
        number_of_elections = len(self.election_result_service.get_election_years())
        if number_of_elections == 0:
            raise ZeroDivisionError("number_of_elections found to be zero")
        return {locale: correct_predictions / number_of_elections for locale, correct_predictions in correct_predictions.items()}

    def sum_correct_predictions_by_locale(self, election_results):
        locale_predictions = self.initialize_locale_dict(election_results)
        for election_result in election_results:
            if self.was_prediction_correct(election_result):
                locale_predictions[election_result.locale] += 1
        return locale_predictions

    def initialize_locale_dict(self, election_results):
        locale_dict = dict()
        for election_result in election_results:
            if locale_dict.get(election_result.locale) is None:
                locale_dict[election_result.locale] = 0
        return locale_dict

    def was_prediction_correct(self, election_result):
        nationally_winning_candidate = self.election_result_service.get_nationally_winning_candidate_by_year(election_result.year)
        return nationally_winning_candidate == election_result.candidate
