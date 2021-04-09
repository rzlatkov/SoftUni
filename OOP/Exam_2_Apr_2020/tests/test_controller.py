import unittest

from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard
from project.controller import Controller
from project.player.advanced import Advanced
from project.player.player_repository import PlayerRepository


class TestController(unittest.TestCase):
    def setUp(self):
        self.ctrler = Controller()

    def test_init(self):
        self.assertEqual(self.ctrler.card_repository.cards, [])
        self.assertEqual(self.ctrler.card_repository.count, 0)
        self.assertEqual(self.ctrler.player_repository.players, [])
        self.assertEqual(self.ctrler.player_repository.count, 0)
        self.assertIsInstance(self.ctrler.card_repository, CardRepository)
        self.assertIsInstance(self.ctrler.player_repository, PlayerRepository)

    def test_add_player(self):
        msg = self.ctrler.add_player('Advanced', 'jack')
        self.assertEqual(self.ctrler.player_repository.count, 1)
        self.assertIsInstance(self.ctrler.player_repository.players[0], Advanced)
        self.assertEqual(msg, "Successfully added player of type Advanced with username: jack")

    def test_add_card(self):
        msg = self.ctrler.add_card('Magic', 'drake')
        self.assertEqual(self.ctrler.card_repository.count, 1)
        self.assertIsInstance(self.ctrler.card_repository.cards[0], MagicCard)
        self.assertEqual(msg, "Successfully added card of type MagicCard with name: drake")

    def test_add_player_card(self):
        self.ctrler.add_player('Advanced', 'jack')
        self.ctrler.add_card('Magic', 'drake')
        msg = self.ctrler.add_player_card('jack', 'drake')
        expected = self.ctrler.player_repository.players[0].card_repository.cards
        self.assertIn(self.ctrler.card_repository.cards[0], expected)
        self.assertEqual(msg, "Successfully added card: drake to user: jack")

    def test_fight(self):
        self.ctrler.add_player('Beginner', 'p1')
        self.ctrler.add_player('Beginner', 'p2')
        res = self.ctrler.fight('p1', 'p2')

        self.assertEqual(res, "Attack user health 90 - Enemy user health 90")

    def test_report(self):
        self.ctrler.add_player('Advanced', 'jack')
        self.ctrler.add_card('Magic', 'drake')
        self.ctrler.add_player_card('jack', 'drake')
        msg = self.ctrler.report()
        expected = 'Username: jack - Health: 250 - Cards 1\n### Card: drake - Damage: 5\n'
        self.assertEqual(msg, expected)

    def test_report_no_output(self):
        msg = self.ctrler.report()
        self.assertEqual(msg, '')


if __name__ == '__main__':
    unittest.main()
