class DecorationRepository:
    def __init__(self):
        self.decorations = []

    def add(self, decoration):  # obj
        self.decorations.append(decoration)

    def remove(self, decoration):  # obj
        if decoration in self.decorations:
            self.decorations.remove(decoration)
            return True
        return False

    def find_by_type(self, decoration_type: str):
        found = [dec for dec in self.decorations if dec.__class__.__name__ == decoration_type]
        if found:
            return found[0]
        return "None"
