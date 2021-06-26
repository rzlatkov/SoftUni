from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type != "FreshwaterAquarium" and aquarium_type != "SaltwaterAquarium":
            return "Invalid aquarium type."

        if aquarium_type == "FreshwaterAquarium":
            aquarium = FreshwaterAquarium(aquarium_name)
        else:
            aquarium = SaltwaterAquarium(aquarium_name)

        self.aquariums.append(aquarium)
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str):
        if decoration_type != "Ornament" and decoration_type != "Plant":
            return "Invalid decoration type."

        if decoration_type == "Ornament":
            decoration = Ornament()
        else:
            decoration = Plant()

        self.decorations_repository.add(decoration)
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        aqua_found = [aqua for aqua in self.aquariums if aquarium_name == aqua.name]
        dec = self.decorations_repository.find_by_type(decoration_type)

        if dec == "None":
            return f"There isn't a decoration of type {decoration_type}."

        if aqua_found:
            aqua = aqua_found[0]
            aqua.add_decoration(dec)
            self.decorations_repository.remove(dec)
            return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        if fish_type != "FreshwaterFish" and fish_type != "SaltwaterFish":
            return f"There isn't a fish of type {fish_type}."

        if fish_type == "FreshwaterFish":
            fish = FreshwaterFish(fish_name, fish_species, price)
        else:
            fish = SaltwaterFish(fish_name, fish_species, price)

        for aqua in self.aquariums:
            if aqua.name == aquarium_name:
                return aqua.add_fish(fish)

    def feed_fish(self, aquarium_name: str):
        for aqua in self.aquariums:
            if aqua.name == aquarium_name:
                for f in aqua.fish:
                    f.eat()
                return f"Fish fed: {len(aqua.fish)}"
        return f"Fish fed: 0"

    def calculate_value(self, aquarium_name: str):
        fish_prices = 0
        dec_prices = 0
        for aqua in self.aquariums:
            if aqua.name == aquarium_name:
                for dec in aqua.decorations:
                    dec_prices += dec.price
                for f in aqua.fish:
                    fish_prices += f.price
            break

        total = fish_prices + dec_prices
        return f"The value of Aquarium {aquarium_name} is {total:.2f}."

    def report(self):
        output = ''
        for aqua in self.aquariums:
            output += aqua.__str__()
            output += '\n'

        return output.rstrip('\n')


ctrl = Controller()

print(ctrl.add_aquarium('FreshwaterAquarium', 'test'))
print(ctrl.add_aquarium('FreshwaterAquarium', 'test2'))
print(ctrl.add_aquarium('kek', 'test3'))

print(ctrl.add_decoration('Ornament'))
print(ctrl.add_decoration('nike'))

print(ctrl.insert_decoration('test', 'nike'))
print(ctrl.insert_decoration('test', 'Ornament'))

print(ctrl.add_fish('test', 'kek', 'test4', 'idk', 12))
print(ctrl.add_fish('test', 'SaltwaterFish', 'cmon', 'idk', 20))
print(ctrl.add_fish('test', 'FreshwaterFish', 'test4', 'idk', 12))
print(ctrl.add_fish('test', 'FreshwaterFish', 'test5', 'idsk', 12))

print(ctrl.feed_fish('test'))
print(ctrl.calculate_value('test'))


print(ctrl.report())
