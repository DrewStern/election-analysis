from src.services.election_result_service import ElectionResultService
from src.services.locality_result_service import LocalityResultService


class PredictionAnalysisService:
    def __init__(self, election_result_service: ElectionResultService, locality_result_service: LocalityResultService):
        self.election_result_service = election_result_service
        self.locality_result_service = locality_result_service

    def find_locales_with_prediction_rate_above(self, prediction_rate_by_locale, prediction_rate_lower_cutoff):
        return [locale for locale in prediction_rate_by_locale if prediction_rate_by_locale[locale] >= prediction_rate_lower_cutoff]

    def find_locales_with_prediction_rate_below(self, prediction_rate_by_locale, prediction_rate_upper_cutoff):
        return [locale for locale in prediction_rate_by_locale if prediction_rate_by_locale[locale] <= prediction_rate_upper_cutoff]

    def get_locale_prediction_ranking(self):
        unsorted_prediction_rate = self.get_prediction_rate_by_locale()
        sorted_prediction_rate = sorted(unsorted_prediction_rate.items(), key=lambda pred_rate: pred_rate[1], reverse=True)
        return list(map(lambda locality: locality[0], sorted_prediction_rate))

    def get_prediction_rate_by_locale(self):
        correct_predictions = self.sum_correct_predictions_by_locale()
        number_of_elections = len(self.election_result_service.get_election_years())
        if number_of_elections == 0:
            raise ZeroDivisionError("number_of_elections should be > 0")
        return {locale: correct_predictions / number_of_elections for locale, correct_predictions in correct_predictions.items()}

    def sum_correct_predictions_by_locale(self):
        years = self.election_result_service.get_election_years()
        localities = self.locality_result_service.get_localities()
        locale_predictions = dict.fromkeys(localities, 0)
        for year in years:
            nation_winner = self.election_result_service.get_nationally_winning_candidate_by_year(year)
            for locality in localities:
                county = locality.split(',')[0]
                state = locality.split(',')[1]
                county_winner = self.election_result_service.get_winning_candidate_for_election(year, county, state)
                if county_winner == nation_winner:
                    locale_predictions[locality] += 1
        return locale_predictions
