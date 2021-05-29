class ElectionResult:
    def __init__(self, data):
        self.year = data[0]
        self.state = data[1]
        self.candidate = data[2].replace(",", "")
        self.party = data[3]
        self.candidatevotes = data[4]
        self.totalvotes = data[5]
        if len(data) > 6:
            self.county = data[6]
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

    def is_from_election(self, year, county, state):
        return self.year == year and self.county == county and self.state == state

    def is_not_from_election(self, year, county, state):
        return not self.is_from_election(year, county, state)
