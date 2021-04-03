from project.vehicle import Vehicle
import unittest


class TestVehicle(unittest.TestCase):
    fuel = 10
    hp = 100
    capacity = fuel
    consumption = 1.25

    def setUp(self):
        self.vehicle = Vehicle(10, 100)

    def test_init(self):
        self.assertEqual(self.fuel, self.vehicle.fuel)
        self.assertEqual(self.hp, self.vehicle.horse_power)
        self.assertEqual(self.capacity, self.vehicle.capacity)
        self.assertEqual(self.consumption, self.vehicle.fuel_consumption)

    def test_drive_fuel_not_enough(self):
        with self.assertRaises(Exception) as exc:
            self.vehicle.drive(10)
        self.assertEqual(str(exc.exception), 'Not enough fuel')

    def test_drive_fuel_enough(self):
        self.vehicle.drive(5)
        self.assertEqual(self.vehicle.fuel, 3.75)

    def test_refuel_fuel_too_much(self):
        with self.assertRaises(Exception) as exc:
            self.vehicle.refuel(5)
        self.assertEqual(str(exc.exception), 'Too much fuel')

    def test_refuel_fuel_enough(self):
        self.vehicle.drive(5)
        self.vehicle.refuel(5)
        self.assertEqual(self.vehicle.fuel, 8.75)

    def test_str_representation(self):
        output = "The vehicle has 100 horse power with 10 fuel left and 1.25 fuel consumption"
        self.assertEqual(str(self.vehicle), output)


if __name__ == '__main__':
    unittest.main()
