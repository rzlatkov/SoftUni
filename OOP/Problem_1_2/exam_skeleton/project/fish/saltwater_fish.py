from project.fish.base_fish import BaseFish

# THIS FISH COULD ONLY LIVE IN SALTWATERAQUARIUM !!!


class SaltwaterFish(BaseFish):
    def __init__(self, name, species, price):
        super().__init__(name=name, species=species, size=5, price=price)

    def eat(self):
        self.size += 2
