import unittest

from project.card.card_repository import CardRepository
from project.player.advanced import Advanced


class TestAdvanced(unittest.TestCase):
    def setUp(self):
        self.adv = Advanced('joe')

    def test_init(self):
        self.assertEqual(self.adv.health, 250)
        self.assertEqual(self.adv.username, 'joe')
        self.assertEqual(self.adv.card_repository.count, 0)
        self.assertEqual(self.adv.card_repository.cards, [])
        self.assertIsInstance(self.adv.card_repository, CardRepository)
        self.assertFalse(self.adv.is_dead)

    def test_health_raises_exception(self):
        self.adv.health = 5
        with self.assertRaises(ValueError) as exc:
            self.adv.take_damage(10)
        self.assertEqual(str(exc.exception), "Player's health bonus cannot be less than zero.")

    def test_username_raises_exception(self):
        with self.assertRaises(ValueError) as exc:
            self.adv.username = ''
        self.assertEqual(str(exc.exception), "Player's username cannot be an empty string.")

    def test_is_dead_true(self):
        self.adv.take_damage(250)
        self.assertTrue(self.adv.is_dead)

    # def test_is_dead_false(self):
    #     self.assertEqual(self.adv.is_dead, False)

    def test_take_damage_raises_exception(self):
        with self.assertRaises(ValueError) as exc:
            self.adv.take_damage(-1)
        self.assertEqual(str(exc.exception), "Damage points cannot be less than zero.")

    def test_take_damage(self):
        self.adv.take_damage(5)
        self.assertEqual(self.adv.health, 245)


if __name__ == '__main__':
    unittest.main()
