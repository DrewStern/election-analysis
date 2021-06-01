class ElectionResult:
    def __init__(self, year, state, candidate, party, candidatevotes, totalvotes, county=None):
        self.year = year
        self.state = state
        self.candidate = candidate.replace(",", "")
        self.party = party
        self.candidatevotes = candidatevotes
        self.totalvotes = totalvotes
        if county is not None:
            self.county = county
            self.locale = self.county + "," + self.state

    def __str__(self):
        return "year: " + self.year + "," + "state: " + self.state + "," + "candidate: " + self.candidate + "," + "candidatevotes: " + self.candidatevotes

    def is_valid(self):
        return self.candidate != "" and self.candidatevotes.lower() != "na"

    def is_not_valid(self):
        return not self.is_valid()

    def is_major_party(self):
        return self.party.lower() == "republican" or self.party.lower() == "democrat"

    def is_not_major_party(self):
        return not self.is_major_party()
