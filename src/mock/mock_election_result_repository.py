from src.election_result import ElectionResult


class MockElectionResultRepository:
    def get_election_results(self):
        return [
            ElectionResult(["1993", "MO", "Fake Candidate 1", "Democrat", "120", "21000000", "County 1"]),
            ElectionResult(["1993", "MO", "Fake Candidate 2", "Republican", "6900", "21000000", "County 1"]),

            ElectionResult(["1993", "MO", "Fake Candidate 1", "Democrat", "451", "21000000", "County 2"]),
            ElectionResult(["1993", "MO", "Fake Candidate 2", "Republican", "6900", "21000000", "County 2"]),

            ElectionResult(["1993", "MO", "Fake Candidate 1", "Democrat", "451", "21000000", "County 3"]),
            ElectionResult(["1993", "MO", "Fake Candidate 2", "Republican", "6900", "21000000", "County 3"]),

            ElectionResult(["1997", "FK", "Fake Candidate 1", "Democrat", "121111", "22000000", "County 1"]),
            ElectionResult(["1997", "FK", "Fake Candidate 2", "Republican", "1901", "22000000", "County 1"]),

            ElectionResult(["1997", "FK", "Fake Candidate 1", "Democrat", "9901", "22000000", "County 2"]),
            ElectionResult(["1997", "FK", "Fake Candidate 2", "Republican", "12321", "22000000", "County 2"]),

            ElectionResult(["1997", "FK", "Fake Candidate 1", "Democrat", "421", "22000000", "County 3"]),
            ElectionResult(["1997", "FK", "Fake Candidate 2", "Republican", "6901", "22000000", "County 3"]),

            ElectionResult(["2001", "MO", "Fake Candidate 1", "Democrat", "120", "21000000", "County 1"]),
            ElectionResult(["2001", "MO", "Fake Candidate 2", "Republican", "6900", "21000000", "County 1"]),

            ElectionResult(["2001", "MO", "Fake Candidate 1", "Democrat", "451", "21000000", "County 2"]),
            ElectionResult(["2001", "MO", "Fake Candidate 2", "Republican", "6900", "21000000", "County 2"]),

            ElectionResult(["2001", "MO", "Fake Candidate 1", "Democrat", "451", "21000000", "County 3"]),
            ElectionResult(["2001", "MO", "Fake Candidate 2", "Republican", "6900", "21000000", "County 3"]),

            ElectionResult(["2005", "FK", "Fake Candidate 1", "Democrat", "121111", "22000000", "County 1"]),
            ElectionResult(["2005", "FK", "Fake Candidate 2", "Republican", "1901", "22000000", "County 1"]),

            ElectionResult(["2005", "FK", "Fake Candidate 1", "Democrat", "9901", "22000000", "County 2"]),
            ElectionResult(["2005", "FK", "Fake Candidate 2", "Republican", "12321", "22000000", "County 2"]),

            ElectionResult(["2005", "FK", "Fake Candidate 1", "Democrat", "421", "22000000", "County 3"]),
            ElectionResult(["2005", "FK", "Fake Candidate 2", "Republican", "6901", "22000000", "County 3"]),
        ]

    def get_nationally_winning_candidates_by_year(self):
        nationally_winning_candidates_by_year = dict()
        nationally_winning_candidates_by_year["1993"] = "Fake Candidate 1"
        nationally_winning_candidates_by_year["1997"] = "Fake Candidate 1"
        nationally_winning_candidates_by_year["2001"] = "Fake Candidate 1"
        nationally_winning_candidates_by_year["2005"] = "Fake Candidate 1"
        return nationally_winning_candidates_by_year

    def get_nationally_losing_candidates_by_year(self):
        nationally_losing_candidates_by_year = dict()
        nationally_losing_candidates_by_year["1993"] = "Fake Candidate 2"
        nationally_losing_candidates_by_year["1997"] = "Fake Candidate 2"
        nationally_losing_candidates_by_year["2001"] = "Fake Candidate 2"
        nationally_losing_candidates_by_year["2005"] = "Fake Candidate 2"
        return nationally_losing_candidates_by_year