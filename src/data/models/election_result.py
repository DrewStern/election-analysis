from src.data.models.election_event import ElectionEvent
from dataclasses import dataclass


@dataclass
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

    def __eq__(self, other):
        return isinstance(other, ElectionResult) \
            and self.election_event == other.election_event \
            and self.candidate == other.candidate \
            and self.party == other.party \
            and self.candidatevotes == other.candidatevotes

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
