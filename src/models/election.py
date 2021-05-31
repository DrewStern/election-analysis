class Election:
    def __init__(self, year, state, county):
        self.year = year
        self.state = state
        self.county = county
        self.locale = county + "," + state

    def __str__(self):
        return "{0}, {1}".format(self.year, self.locale)
