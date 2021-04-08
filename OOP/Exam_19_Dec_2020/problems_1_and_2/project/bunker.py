class Bunker:
    def __init__(self):
        self.survivors = []
        self.supplies = []
        self.medicine = []

    @property
    def food(self):
        food_objects = []
        for obj in self.supplies:
            if obj.__class__.__name__ == 'FoodSupply':
                food_objects.append(obj)

        if len(food_objects) == 0:
            raise IndexError('There are no food supplies left!')
        return food_objects

    @property
    def water(self):
        water_objects = []
        for obj in self.supplies:
            if obj.__class__.__name__ == 'WaterSupply':
                water_objects.append(obj)

        if len(water_objects) == 0:
            raise IndexError('There are no water supplies left!')
        return water_objects

    @property
    def painkillers(self):
        painkiller_objects = []
        for obj in self.medicine:
            if obj.__class__.__name__ == 'Painkiller':
                painkiller_objects.append(obj)

        if not painkiller_objects:
            raise IndexError('There are no painkillers left!')
        return painkiller_objects

    @property
    def salves(self):
        salve_objects = []
        for obj in self.medicine:
            if obj.__class__.__name__ == 'Painkiller':
                salve_objects.append(obj)

        if not salve_objects:
            raise IndexError('There are no salves left!')
        return salve_objects

    def add_survivor(self, survivor):
        if survivor in self.survivors:
            raise ValueError(f'Survivor with name {survivor.name} already exists.')
        self.survivors.append(survivor)

    def add_supply(self, supply):
        self.supplies.append(supply)

    def add_medicine(self, medicine):
        self.medicine.append(medicine)

    def heal(self, survivor, medicine_type):
        if survivor.needs_healing:
            if medicine_type == 'Painkiller':
                painkillers = self.painkillers
                painkiller = painkillers[-1]
                painkiller.apply(survivor)
                self.medicine.remove(painkiller)
            elif medicine_type == 'Salve':
                salves = self.salves
                salve = salves[-1]
                salve.apply(survivor)
                self.medicine.remove(salve)
            return f"{survivor.name} healed successfully with {medicine_type}"

    def sustain(self, survivor, sustenance_type):
        if survivor.needs_sustenance:
            if sustenance_type == 'WaterSupply':
                waters = self.water
                water = waters[-1]
                water.apply(survivor)
                self.supplies.remove(water)
            elif sustenance_type == 'FoodSupply':
                foods = self.food
                food = foods[-1]
                food.apply(survivor)
                self.supplies.remove(food)
            return f"{survivor.name} sustained successfully with {sustenance_type}"

    def next_day(self):
        for survivor in self.survivors:
            reduced_needs = survivor.needs - survivor.age * 2
            survivor.needs = reduced_needs
            self.sustain(survivor, 'FoodSupply')
            self.sustain(survivor, 'WaterSupply')
