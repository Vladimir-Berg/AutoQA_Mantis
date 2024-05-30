from sys import maxsize


class Project:

    def __init__(self, name=None, id=None):
        self.id = id
        self.name = name

    def __repr__(self):
        return "Project(%s)" % self.name

    def __eq__(self, other):
        return self.name == other.name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
