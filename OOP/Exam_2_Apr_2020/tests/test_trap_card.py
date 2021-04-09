import unittest

from project.card.trap_card import TrapCard


class TestTrapCard(unittest.TestCase):
    def setUp(self):
        self.trap = TrapCard('dragon')

    def test_init(self):
        self.assertEqual(self.trap.name, 'dragon')
        self.assertEqual(self.trap.health_points, 5)
        self.assertEqual(self.trap.damage_points, 120)

    def test_name_raises_exception(self):
        with self.assertRaises(ValueError) as exc:
            self.trap.name = ''
        self.assertEqual(str(exc.exception), "Card's name cannot be an empty string.")

    def test_dmg_raises_exception(self):
        with self.assertRaises(ValueError) as exc:
            self.trap.damage_points = -1
        self.assertEqual(str(exc.exception), "Card's damage points cannot be less than zero.")

    def test_hp_raises_exception(self):
        with self.assertRaises(ValueError) as exc:
            self.trap.health_points = -1
        self.assertEqual(str(exc.exception), "Card's HP cannot be less than zero.")


if __name__ == '__main__':
    unittest.main()
