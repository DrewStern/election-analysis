class Candidate:
    def __init__(self, name, party):
        self.name = name.replace(",", "")
        self.party = party

    def __str__(self):
        return "{0}, {1}".format(self.name, self.party)

    def is_valid(self):
        return self.name != "" and self.party != ""

    def is_not_valid(self):
        return not self.is_valid()

    def is_major_party(self):
        return self.party.lower() == "republican" or self.party.lower() == "democrat"

    def is_not_major_party(self):
        return not self.is_major_party()
