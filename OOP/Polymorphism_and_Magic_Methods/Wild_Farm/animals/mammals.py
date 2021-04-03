from Wild_Farm.food import Meat, Vegetable, Fruit, Seed
from Wild_Farm.animals.animal import Mammal


class Mouse(Mammal):
    WEIGHT_INCREASE = 0.10

    def __init__(self, name, weight, living_region):
        super().__int__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        animal_type = self.__class__.__name__
        return f"{animal_type} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"

    def make_sound(self):
        return f"Squeak"

    def feed(self, food):
        food_type = food.__class__.__name__
        if food_type == "Vegetable" or food_type == "Fruit":
            self.food_eaten += food.quantity
            self.weight += food.quantity * Mouse.WEIGHT_INCREASE
        else:
            return f"{self.__class__.__name__} does not eat {food_type}!"


class Dog(Mammal):
    WEIGHT_INCREASE = 0.40

    def __init__(self, name, weight, living_region):
        super().__int__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        animal_type = self.__class__.__name__
        return f"{animal_type} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"

    def make_sound(self):
        return f"Woof!"

    def feed(self, food):
        food_type = food.__class__.__name__
        if not food_type == "Meat":
            return f"{self.__class__.__name__} does not eat {food_type}!"
        self.food_eaten += food.quantity
        self.weight += food.quantity * Dog.WEIGHT_INCREASE


class Cat(Mammal):
    WEIGHT_INCREASE = 0.30

    def __init__(self, name, weight, living_region):
        super().__int__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        animal_type = self.__class__.__name__
        return f"{animal_type} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"

    def make_sound(self):
        return f"Meow"

    def feed(self, food):
        food_type = food.__class__.__name__
        if food_type == "Vegetable" or food_type == "Meat":
            self.food_eaten += food.quantity
            self.weight += food.quantity * Cat.WEIGHT_INCREASE
        else:
            return f"{self.__class__.__name__} does not eat {food_type}!"


class Tiger(Mammal):
    WEIGHT_INCREASE = 1.00

    def __init__(self, name, weight, living_region):
        super().__int__(name, weight)
        self.living_region = living_region

    def __repr__(self):
        animal_type = self.__class__.__name__
        return f"{animal_type} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]"

    def make_sound(self):
        return f"ROAR!!!"

    def feed(self, food):
        food_type = food.__class__.__name__
        if not food_type == "Meat":
            return f"{self.__class__.__name__} does not eat {food_type}!"
        self.food_eaten += food.quantity
        self.weight += food.quantity * Tiger.WEIGHT_INCREASE


# m = Mouse("Harry", 10, 'Africa')
# veg = Vegetable(3)
# fruit = Fruit(5)
# meat = Meat(1)
# print(m)
# print(m.make_sound())
# m.feed(veg)
# m.feed(fruit)
# print(m.feed(meat))
# print(m)
