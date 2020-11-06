class ElectionResult:
    def __init__(self, data):
        self.year = data[0]
        self.state = data[1]
        self.candidate = data[2]
        self.party = data[3]
        self.writein = data[4]
        self.candidatevotes = data[5]
        self.totalvotes = data[6]

    def __str__(self):
        return "year: " + self.year + "," + "state: " + self.state + "," + "candidate: " + self.candidate + "," + "candidatevotes: " + self.candidatevotes