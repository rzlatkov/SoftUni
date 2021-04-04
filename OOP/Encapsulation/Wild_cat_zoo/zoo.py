class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__animal_capacity > len(self.animals):
            if price > self.__budget:
                return "Not enough budget"
        if self.__animal_capacity <= len(self.animals):
            return "Not enough space for animal"
        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        found = [w for w in self.workers if w.name == worker_name]
        if found:
            worker = found[0]
            self.workers.remove(worker)
            return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        salaries = [w.salary for w in self.workers]
        total = sum(salaries)
        if self.__budget < total:
            return "You have no budget to pay your workers. They are unhappy"
        self.__budget -= total
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        tends = [a.needs for a in self.animals]
        total = sum(tends)
        if self.__budget < total:
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= total
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        output = f"You have {len(self.animals)} animals\n"
        lions = [l for l in self.animals if l.__class__.__name__ == 'Lion']
        tigers = [t for t in self.animals if t.__class__.__name__ == 'Tiger']
        cheetahs = [ch for ch in self.animals if ch.__class__.__name__ == 'Cheetah']
        output += f"----- {len(lions)} Lions:\n"
        for l in lions:
            output += l.__repr__() + '\n'
        output += f"----- {len(tigers)} Tigers:\n"
        for t in tigers:
            output += t.__repr__() + '\n'
        output += f"----- {len(cheetahs)} Cheetahs:\n"
        for ch in cheetahs:
            output += ch.__repr__() + '\n'

        return output.rstrip()

    def workers_status(self):
        output = f"You have {len(self.workers)} workers\n"
        keepers = [k for k in self.workers if k.__class__.__name__ == 'Keeper']
        caretakers = [c for c in self.workers if c.__class__.__name__ == 'Caretaker']
        vets = [v for v in self.workers if v.__class__.__name__ == 'Vet']
        output += f"----- {len(keepers)} Keepers:\n"
        for k in keepers:
            output += k.__repr__() + '\n'
        output += f"----- {len(caretakers)} Caretakers:\n"
        for c in caretakers:
            output += c.__repr__() + '\n'
        output += f"----- {len(vets)} Vets:\n"
        for v in vets:
            output += v.__repr__() + '\n'

        return output.rstrip()
