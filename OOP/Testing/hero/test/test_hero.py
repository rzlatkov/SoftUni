import unittest
from project.hero import Hero


class TestHero(unittest.TestCase):
    name = 'joe'
    lvl = 10
    hp = 15.0
    dmg = 20.0

    def setUp(self):
        self.hero = Hero(
            username=self.name,
            level=self.lvl,
            health=self.hp,
            damage=self.dmg
        )

    def test_init(self):
        self.assertEqual(self.hero.username, self.name)
        self.assertEqual(self.hero.level, self.lvl)
        self.assertEqual(self.hero.health, self.hp)
        self.assertEqual(self.hero.damage, self.dmg)

    def test_battle_cannot_fight_yourself(self):
        enemy = self.hero
        with self.assertRaises(Exception) as exc:
            self.hero.battle(enemy)
        self.assertEqual(str(exc.exception), 'You cannot fight yourself')

    def test_battle_hero_health_zero(self):
        enemy = Hero('enemy', 5, 15.0, 25.0)
        self.hero.health = 0
        with self.assertRaises(ValueError) as exc:
            self.hero.battle(enemy)
        self.assertEqual(str(exc.exception), 'Your health is lower than or equal to 0. You need to rest')

    def test_battle_hero_health_lower_than_zero(self):
        enemy = Hero('enemy', 5, 15.0, 25.0)
        self.hero.health = -5
        with self.assertRaises(ValueError) as exc:
            self.hero.battle(enemy)
        self.assertEqual(str(exc.exception), 'Your health is lower than or equal to 0. You need to rest')

    def test_battle_enemy_health_zero(self):
        enemy = Hero('enemy', 5, -1.0, 25.0)
        enemy.health = 0
        with self.assertRaises(ValueError) as exc:
            self.hero.battle(enemy)
        self.assertEqual(str(exc.exception), f'You cannot fight {enemy.username}. He needs to rest')

    def test_battle_enemy_health_lower_than_zero(self):
        enemy = Hero('enemy', 5, 0.0, 25.0)
        enemy.health = -5
        with self.assertRaises(ValueError) as exc:
            self.hero.battle(enemy)
        self.assertEqual(str(exc.exception), f'You cannot fight {enemy.username}. He needs to rest')

    def test_battle_draw(self):
        enemy = Hero('enemy', 5, 15.0, 25.0)
        result = self.hero.battle(enemy)

        self.assertEqual(result, 'Draw')

    def test_check_health_after_draw(self):
        enemy = Hero('enemy', 5, 15.0, 25.0)
        self.hero.battle(enemy)

        self.assertEqual(self.hero.health, -110)
        self.assertEqual(enemy.health, -185)

    def test_check_enemy_health_after_win(self):
        enemy = Hero('enemy', 1, 1.0, 1.0)
        self.hero.battle(enemy)

        self.assertEqual(enemy.health, -199)

    def test_check_hero_health_after_lose(self):
        enemy = Hero('enemy', 100, 100.0, 100.0)
        self.hero.damage = 1
        self.hero.level = 1
        self.hero.health = 1
        self.hero.battle(enemy)

        self.assertEqual(self.hero.health, -9999.0)

    def test_battle_you_win(self):
        enemy = Hero('enemy', 1, 1.0, 1.0)
        result = self.hero.battle(enemy)

        self.assertEqual(result, 'You win')
        self.assertEqual(self.hero.health, 19)
        self.assertEqual(self.hero.level, 11)
        self.assertEqual(self.hero.damage, 25)

    def test_battle_you_lose(self):
        enemy = Hero('enemy', 100, 100.0, 100.0)
        self.hero.damage = 1
        self.hero.level = 1
        self.hero.health = 1
        result = self.hero.battle(enemy)

        self.assertEqual(result, 'You lose')
        self.assertEqual(enemy.health, 104.0)
        self.assertEqual(enemy.level, 101)
        self.assertEqual(enemy.damage, 105.0)

    def test_str_representation(self):
        output = f"Hero {self.name}: {self.lvl} lvl\nHealth: {self.hp}\nDamage: {self.dmg}\n"
        self.assertEqual(self.hero.__str__(), output)


if __name__ == '__main__':
    unittest.main()
