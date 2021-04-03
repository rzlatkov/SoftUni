from mammal.project.mammal import Mammal

import unittest


class TestMammal(unittest.TestCase):
    name = 'Sharo'
    mammal_type = 'dog'
    sound = 'woof'
    kingdom = 'animals'

    def setUp(self):
        self.mammal = Mammal('Sharo', 'dog', 'woof')

    def test_init(self):
        self.assertEqual(self.name, self.mammal.name)
        self.assertEqual(self.mammal_type, self.mammal.type)
        self.assertEqual(self.sound, self.mammal.sound)
        self.assertEqual(self.kingdom, self.mammal._Mammal__kingdom)

    def test_make_sound(self):
        self.assertEqual(self.mammal.make_sound(), 'Sharo makes woof')

    def test_get_kingdom(self):
        self.assertEqual(self.mammal.get_kingdom(), 'animals')

    def test_info(self):
        self.assertEqual(self.mammal.info(), 'Sharo is of type dog')


if __name__ == '__main__':
    unittest.main()
