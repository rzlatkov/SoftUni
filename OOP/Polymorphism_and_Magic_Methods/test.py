from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def __init__(self, make, hp, speed):
        self.make = make
        self.hp = hp
        self.speed = speed
        self.nitrous = False

    @abstractmethod
    def make_sound(self):
        pass


class Car(Vehicle):
    def __init__(self, make, hp, speed, wheelbase):
        super().__init__(make, hp, speed)
        self.wheelbase = wheelbase

    def make_sound(self):
        return "RATATA"

    def __repr__(self):
        return f"{self.make} has {self.hp} hp and {self.speed} top speed! It's also a {self.wheelbase}. " \
               f"Nitrous={self.nitrous}"


bmw = Car('bmw', 510, '320', 'RWD')
print(bmw)
print(bmw.make_sound())


# class HyperCar(Car):
#     def __init__(self, name, hp, speed, wheelbase, nitrous):
#         super().__init__(name, hp, speed, wheelbase)
#         self.nitrous = nitrous
#
#     def make_sound(self):
#         return "VROOM"
#
#     def __repr__(self):
#         return super().__repr__() + 'It is on nitrous!'


# dragster = HyperCar('billet', 1500, '400', 'RWD', True)
# print(dragster)
# print(dragster.make_sound())
# print(HyperCar.mro())
