from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCoupleWithChildren(Room):
    def __init__(self, family_name, salary_one, salary_two, *children):
        super().__init__(family_name, salary_one + salary_two, 2 + len(children))
        self.room_cost = 30
        self.children = [ch for ch in children]
        self.appliances = []

        for _ in range(2 + len(self.children)):
            self.appliances.append(TV())
            self.appliances.append(Fridge())
            self.appliances.append(Laptop())

        self.calculate_expenses(self.children, self.appliances)
