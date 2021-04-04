class Hardware:
    def __init__(self, name, type, capacity, memory):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []
        self.available_cap = self.capacity
        self.available_mem = self.memory

    def install(self, software):
        if software.capacity_consumption <= self.available_cap and software.memory_consumption <= self.available_mem:
            self.available_cap -= software.capacity_consumption
            self.available_mem -= software.memory_consumption
            self.software_components.append(software)
        else:
            raise Exception('Software cannot be installed')

    def uninstall(self, software):
        if software in self.software_components:
            self.available_cap += software.capacity_consumption
            self.available_mem += software.memory_consumption
            self.software_components.remove(software)
