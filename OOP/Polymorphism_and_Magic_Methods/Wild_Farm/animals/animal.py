from abc import ABC, abstractmethod


class Animal(ABC):
    def __int__(self, name, weight):
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def feed(self, food):
        pass


class Bird(Animal, ABC):
    # def __init__(self, name, weight, wing_size):
    #     super().__init__(name, weight)
    #     self.wing_size = wing_size

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def feed(self, food):
        pass


class Mammal(Animal, ABC):
    # def __init__(self, name, weight, living_region):
    #     super().__init__(name, weight)
    #     self.living_region = living_region

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def feed(self, food):
        pass
