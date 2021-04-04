class Equipment:
    next_id = 1

    def __init__(self, name):
        self.name = name
        self.id = Equipment.next_id
        Equipment.next_id += 1

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"

    @staticmethod
    def get_next_id():
        return Equipment.next_id
