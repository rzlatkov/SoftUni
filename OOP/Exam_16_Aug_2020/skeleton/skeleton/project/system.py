from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name, capacity, memory):
        System._hardware.append(PowerHardware(name, capacity, memory))

    @staticmethod
    def register_heavy_hardware(name, capacity, memory):
        System._hardware.append(HeavyHardware(name, capacity, memory))

    @staticmethod
    def register_express_software(hardware_name, name, capacity_consumption, memory_consumption):
        found = [obj for obj in System._hardware if obj.name == hardware_name]
        if found:
            sw = ExpressSoftware(name, capacity_consumption, memory_consumption)
            try:
                found[0].install(sw)
                System._software.append(sw)
            except Exception as exc:
                return str(exc)
        else:
            return "Hardware does not exist"

    @staticmethod
    def register_light_software(hardware_name, name, capacity_consumption, memory_consumption):
        found = [obj for obj in System._hardware if obj.name == hardware_name]
        if found:
            sw = LightSoftware(name, capacity_consumption, memory_consumption)
            try:
                found[0].install(sw)
                System._software.append(sw)
            except Exception as exc:
                return str(exc)
        else:
            return "Hardware does not exist"

    @staticmethod
    def release_software_component(hardware_name, software_name):
        found_hw = [obj for obj in System._hardware if obj.name == hardware_name]
        found_sw = [obj for obj in System._software if obj.name == software_name]
        if found_sw and found_hw:
            found_hw[0].uninstall(found_sw[0])
            System._software.remove(found_sw[0])
        else:
            return "Some of the components do not exist"

    @staticmethod
    def analyze():
        output = 'System Analysis\n'
        output += f'Hardware Components: {len(System._hardware)}\n'
        output += f"Software Components: {len(System._software)}\n"
        total_memory = 0
        total_capacity = 0
        used_memory = 0
        used_capacity = 0
        for obj in System._hardware:
            total_memory += obj.memory
            total_capacity += obj.capacity
            for sw_obj in obj.software_components:
                used_memory += sw_obj.memory_consumption
                used_capacity += sw_obj.capacity_consumption
        output += f"Total Operational Memory: {used_memory} / {total_memory}\n"
        output += f"Total Capacity Taken: {used_capacity} / {total_capacity}"
        return output

    @staticmethod
    def system_split():
        output = ''
        for obj in System._hardware:
            express_sw_count = 0
            light_sw_count = 0
            memory_usage = 0
            capacity_usage = 0
            output += f'Hardware Component - {obj.name}\n'
            sw_installed = []
            for sw_obj in obj.software_components:
                sw_installed.append(sw_obj.name)
                if sw_obj.type == 'Express':
                    express_sw_count += 1
                elif sw_obj.type == 'Light':
                    light_sw_count += 1
                memory_usage += sw_obj.memory_consumption
                capacity_usage += sw_obj.capacity_consumption
            output += f"Express Software Components: {express_sw_count}\n"
            output += f"Light Software Components: {light_sw_count}\n"
            output += f"Memory Usage: {memory_usage} / {obj.memory}\n"
            output += f"Capacity Usage: {capacity_usage} / {obj.capacity}\n"
            output += f"Type: {obj.type}\n"
            if sw_installed:
                output += f"Software Components: {', '.join(sw_installed)}"
            else:
                output += f"Software Components: None"
        return output
