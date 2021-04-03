from Wild_Farm.food import Meat, Vegetable, Fruit, Seed
from Wild_Farm.animals.animal import Bird


class Owl(Bird):
    WEIGHT_INCREASE = 0.25

    def __init__(self, name, weight, wing_size):
        super().__int__(name, weight)
        self.wing_size = wing_size

    def __repr__(self):
        animal_type = self.__class__.__name__
        return f"{animal_type} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"

    def make_sound(self):
        return f"Hoot Hoot"

    def feed(self, food):
        food_type = food.__class__.__name__
        if food_type != "Meat":
            return f"{self.__class__.__name__} does not eat {food_type}!"
        self.food_eaten += food.quantity
        self.weight += food.quantity * Owl.WEIGHT_INCREASE


class Hen(Bird):
    WEIGHT_INCREASE = 0.35

    def __init__(self, name, weight, wing_size):
        super().__int__(name, weight)
        self.wing_size = wing_size

    def __repr__(self):
        animal_type = self.__class__.__name__
        return f"{animal_type} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"

    def make_sound(self):
        return f"Cluck"

    def feed(self, food):
        self.food_eaten += food.quantity
        self.weight += food.quantity * Hen.WEIGHT_INCREASE


# hen = Hen("Harry", 10, 10)
# veg = Vegetable(3)
# fruit = Fruit(5)
# meat = Meat(1)
# print(hen)
# print(hen.make_sound())
# hen.feed(veg)
# hen.feed(fruit)
# hen.feed(meat)
# print(hen)
