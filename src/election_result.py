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

    def is_major_party(self):
        return self.party == "republican" or self.party == "democrat"

    def is_not_major_party(self):
        return not self.is_major_party()

    def is_from_same_election(self, year, county, state):
        return self.year == year and self.county == county and self.state == state
