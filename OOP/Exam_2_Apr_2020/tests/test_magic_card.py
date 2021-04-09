import unittest

from project.card.magic_card import MagicCard


class TestMagicCard(unittest.TestCase):
    def setUp(self):
        self.magic = MagicCard('dragon')

    def test_init(self):
        self.assertEqual(self.magic.name, 'dragon')
        self.assertEqual(self.magic.health_points, 80)
        self.assertEqual(self.magic.damage_points, 5)

    def test_name_raises_exception(self):
        with self.assertRaises(ValueError) as exc:
            self.magic.name = ''
        self.assertEqual(str(exc.exception), "Card's name cannot be an empty string.")

    def test_dmg_raises_exception(self):
        with self.assertRaises(ValueError) as exc:
            self.magic.damage_points = -1
        self.assertEqual(str(exc.exception), "Card's damage points cannot be less than zero.")

    def test_hp_raises_exception(self):
        with self.assertRaises(ValueError) as exc:
            self.magic.health_points = -1
        self.assertEqual(str(exc.exception), "Card's HP cannot be less than zero.")


if __name__ == '__main__':
    unittest.main()
