import unittest

from project.player.advanced import Advanced
from project.player.beginner import Beginner
from project.player.player_repository import PlayerRepository


class TestPlayerRepo(unittest.TestCase):
    def setUp(self):
        self.repo = PlayerRepository()

    def test_init(self):
        self.assertEqual(self.repo.count, 0)
        self.assertEqual(self.repo.players, [])

    def test_add__raises_exception(self):
        pl = Advanced('jack')
        pl2 = Beginner('jack')
        self.repo.add(pl)
        self.assertEqual(self.repo.count, 1)
        with self.assertRaises(ValueError) as exc:
            self.repo.add(pl2)
        self.assertEqual(str(exc.exception), "Player jack already exists!")

    def test_add(self):
        pl = Advanced('jack')
        self.repo.add(pl)
        self.assertEqual(self.repo.count, 1)
        self.assertIn(pl, self.repo.players)

    def test_remove__raises_exception(self):
        with self.assertRaises(ValueError) as exc:
            self.repo.remove('')
        self.assertEqual(str(exc.exception), "Player cannot be an empty string!")

    def test_remove(self):
        pl = Advanced('jack')
        self.repo.add(pl)
        self.assertEqual(self.repo.count, 1)
        self.repo.remove('jack')
        self.assertEqual(self.repo.count, 0)
        self.assertEqual(self.repo.players, [])

    def test_find(self):
        pl = Advanced('jack')
        pl2 = Beginner('joe')
        self.repo.add(pl)
        self.repo.add(pl2)
        result = self.repo.find('joe')
        self.assertEqual(result, pl2)


if __name__ == '__main__':
    unittest.main()
