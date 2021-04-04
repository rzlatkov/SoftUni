from project.hardware.hardware import Hardware


class HeavyHardware(Hardware):
    def __init__(self, name, capacity, memory):
        super().__init__(name, 'Heavy', capacity, memory)
        self.capacity = int(2 * capacity)
        self.memory = int(0.75 * memory)
        self.available_cap = self.capacity
        self.available_mem = self.memory
