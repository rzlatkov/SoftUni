from project.fish.base_fish import BaseFish

# THIS FISH COULD ONLY LEAVE IN FRESHWATERAQUARIUM !!!


class FreshwaterFish(BaseFish):
    def __init__(self, name, species, price):
        super().__init__(name=name, species=species, size=3, price=price)

    def eat(self):
        self.size += 3
