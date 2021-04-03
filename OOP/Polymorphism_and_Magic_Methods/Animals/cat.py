from Animals.animal import Animal


class Cat(Animal):
    def make_sound(self):
        return f"Meow meow!"

    def __repr__(self):
        animal_type = self.__class__.__name__
        return f"This is {self.name}. {self.name} is a {self.age} year old {self.gender} {animal_type}"
