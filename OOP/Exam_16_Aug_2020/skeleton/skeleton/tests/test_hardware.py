import unittest

# from project.hardware.hardware import Hardware
from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.light_software import LightSoftware


class TestHardware(unittest.TestCase):
    def setUp(self) -> None:
        self.heavy = HeavyHardware('nxp', 100, 200)
        self.power = PowerHardware('ti', 200, 300)

    def test_init_heavy(self):
        self.assertEqual(self.heavy.name, 'nxp')
        self.assertEqual(self.heavy.type, 'Heavy')
        self.assertEqual(self.heavy.capacity, 200)
        self.assertEqual(self.heavy.memory, 150)
        self.assertEqual(self.heavy.software_components, [])

    def test_init_power(self):
        self.assertEqual(self.power.name, 'ti')
        self.assertEqual(self.power.type, 'Power')
        self.assertEqual(self.power.capacity, 50)
        self.assertEqual(self.power.memory, 525)
        self.assertEqual(self.power.software_components, [])

    def test_install_heavy(self):
        sw = LightSoftware('unix', 1, 1)
        self.heavy.install(sw)
        self.assertIn(sw, self.heavy.software_components)

    def test_install_heavy_no_space(self):
        sw = LightSoftware('unix', 2000, 2000)
        with self.assertRaises(Exception) as exc:
            self.heavy.install(sw)
        self.assertEqual(str(exc.exception), 'Software cannot be installed')

    def test_install_power(self):
        sw = LightSoftware('unix', 1, 1)
        self.power.install(sw)
        self.assertIn(sw, self.power.software_components)

    def test_install_power_no_space(self):
        sw = LightSoftware('unix', 2000, 2000)
        with self.assertRaises(Exception) as exc:
            self.power.install(sw)
        self.assertEqual(str(exc.exception), 'Software cannot be installed')

    def test_uninstall_heavy_when_sw_in_sw_components(self):
        sw = LightSoftware('unix', 1, 1)
        self.heavy.install(sw)
        self.heavy.uninstall(sw)
        self.assertEqual(self.heavy.software_components, [])

    def test_uninstall_heavy_when_sw_not_in_sw_components(self):
        sw = LightSoftware('unix', 1, 1)
        self.heavy.uninstall(sw)
        self.assertEqual(self.heavy.software_components, [])

    def test_uninstall_power_when_sw_in_sw_components(self):
        sw = LightSoftware('unix', 1, 1)
        self.power.install(sw)
        self.power.uninstall(sw)
        self.assertEqual(self.power.software_components, [])

    def test_uninstall_power_when_sw_not_in_sw_components(self):
        sw = LightSoftware('unix', 1, 1)
        self.power.uninstall(sw)
        self.assertEqual(self.power.software_components, [])


if __name__ == '__main__':
    unittest.main()
