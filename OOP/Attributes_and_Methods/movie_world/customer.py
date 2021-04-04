class Customer:
    def __init__(self, name, age, id):
        self.name = name
        self.age = int(age)
        self.id = int(id)
        self.rented_dvds = []

    def __repr__(self):
        output = f"{self.id}: {self.name} of age {self.age} has {len(self.rented_dvds)} rented DVD's ("
        for dvd in self.rented_dvds:
            output += dvd.name + ', '
        output = output.rstrip(', ')
        output += ')'
        return output