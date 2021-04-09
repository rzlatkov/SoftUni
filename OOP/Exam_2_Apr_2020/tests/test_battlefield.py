import unittest

from project.battle_field import BattleField
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard
from project.player.advanced import Advanced
from project.player.beginner import Beginner


class TestBattleField(unittest.TestCase):
    def setUp(self):
        self.beg = Beginner('joe')  # hp=50
        self.adv = Advanced('jack')  # hp=250
        self.magic = MagicCard('dragon')  # dmg=5; hp=80
        self.trap = TrapCard('dark hole')  # dmg=120; hp=5

        # self.beg.card_repository.add(self.magic)
        # self.adv.card_repository.add(self.trap)

    def test_fight__raises__player_is_dead(self):
        self.beg.card_repository.add(self.magic)
        self.adv.card_repository.add(self.trap)

        self.beg.take_damage(50)
        with self.assertRaises(ValueError) as exc:
            BattleField.fight(self.beg, self.adv)
        self.assertEqual(str(exc.exception), "Player is dead!")

    def test_fight(self):
        self.beg.card_repository.add(self.magic)
        self.adv.card_repository.add(self.trap)

        BattleField.fight(self.beg, self.adv)
        self.assertEqual(self.beg.health, 50)
        self.assertEqual(self.adv.health, 220)
        self.assertEqual(self.magic.damage_points, 35)
        self.assertEqual(self.trap.damage_points, 120)


if __name__ == '__main__':
    unittest.main()
