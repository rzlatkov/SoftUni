from abc import abstractmethod, ABC


class BaseAquarium(ABC):
    @abstractmethod
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity  # the number of fish the aquarium can have
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Aquarium name cannot be an empty string.")
        self.__name = value

    def calculate_comfort(self):
        result = sum([dec.comfort for dec in self.decorations])
        return f"{result:.2f}"

    def add_fish(self, fish):  # obj
        if self.capacity == 0:
            return f"Not enough capacity."

        fish_type = fish.__class__.__name__
        aquarium_type = self.__class__.__name__

        if fish_type == 'FreshwaterFish' or fish_type == 'SaltwaterFish':
            if fish_type[:5] == aquarium_type[:5]:
                self.fish.append(fish)
                self.capacity -= 1
                return f"Successfully added {fish_type} to {self.name}."

        return "Water not suitable."

    def remove_fish(self, fish):  # obj
        self.fish.remove(fish)
        self.capacity += 1

    def add_decoration(self, decoration):  # obj
        self.decorations.append(decoration)

    def feed(self):
        for f in self.fish:
            f.eat()

    def __str__(self):
        output = ''
        output += f"{self.name}\n"
        if len(self.fish) == 0:
            output += f"Fish: none\n"
        else:
            output += "Fish:"
            for f in self.fish:
                output += f" {f.name}"
            output += '\n'
        output += f"Decorations: {len(self.decorations)}\n"
        output += f"Comfort: {self.calculate_comfort()}"

        return output
