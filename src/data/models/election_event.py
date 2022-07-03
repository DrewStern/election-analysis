from dataclasses import dataclass

@dataclass
class ElectionEvent:
    def __init__(self, year, state, county):
        self.year = year
        self.state = state
        self.county = county
        self.locale = self.county + "," + self.state

    def __eq__(self, other):
        if isinstance(other, ElectionEvent):
            return self.year == other.year and self.state == other.state and self.county == other.county
        return False

    def __str__(self):
        return "{0}, {1}, {2}".format(self.year, self.state, self.county)
