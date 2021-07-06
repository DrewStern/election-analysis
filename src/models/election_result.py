from src.models.election_event import ElectionEvent


class ElectionResult:
    def __init__(self, year, state, candidate, party, candidatevotes, totalvotes, county=None):
        self.election_event = ElectionEvent(year, state, county)
        self.year = year
        self.state = state
        if county is not None:
            self.county = county
            self.locale = self.county + "," + self.state
        self.totalvotes = totalvotes

        self.candidate = candidate.replace(",", "")
        self.party = party
        self.candidatevotes = candidatevotes

    def __str__(self):
        return "{0}, {1}, {2}, {3}".format(self.year, self.locale, self.candidate, self.party)

    def is_valid(self):
        return self.candidate != "" and self.candidatevotes.lower() != "na"

    def is_not_valid(self):
        return not self.is_valid()

    def is_major_party(self):
        return self.party.lower() == "republican" or self.party.lower() == "democrat"

    def is_not_major_party(self):
        return not self.is_major_party()
