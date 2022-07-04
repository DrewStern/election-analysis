class TimespaceReducerService:
    def filter_by(self, election_results: ElectionResult[], propertyName, propertyValue):
        matching_results = []
        for election_result in election_results:
            if election_result[propertyName].lower() == propertyValue.lower():
                matching_results.append(election_result)
        return matching_results