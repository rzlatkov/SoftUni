import unittest

from project.player.beginner import Beginner


class TestBeginner(unittest.TestCase):
    def setUp(self):
        self.beg = Beginner('joe')

    def test_init(self):
        self.assertEqual(self.beg.health, 50)
        self.assertEqual(self.beg.username, 'joe')
        self.assertEqual(self.beg.card_repository.count, 0)
        self.assertEqual(self.beg.card_repository.cards, [])

    def test_health_raises_exception(self):
        self.beg.health = 5
        with self.assertRaises(ValueError) as exc:
            self.beg.take_damage(10)
        self.assertEqual(str(exc.exception), "Player's health bonus cannot be less than zero.")

    def test_username_raises_exception(self):
        with self.assertRaises(ValueError) as exc:
            self.beg.username = ''
        self.assertEqual(str(exc.exception), "Player's username cannot be an empty string.")

    def test_is_dead_true(self):
        self.beg.health = 0
        self.assertEqual(self.beg.is_dead, True)

    def test_is_dead_false(self):
        self.assertEqual(self.beg.is_dead, False)

    def test_take_damage_raises_exception(self):
        with self.assertRaises(ValueError) as exc:
            self.beg.take_damage(-1)
        self.assertEqual(str(exc.exception), "Damage points cannot be less than zero.")

    def test_take_damage(self):
        self.beg.take_damage(5)
        self.assertEqual(self.beg.health, 45)


if __name__ == '__main__':
    unittest.main()
