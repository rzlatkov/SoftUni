import unittest

from project.card.card_repository import CardRepository
from project.card.magic_card import MagicCard
from project.card.trap_card import TrapCard


class TestCardRepo(unittest.TestCase):
    def setUp(self):
        self.repo = CardRepository()

    def test_init(self):
        self.assertEqual(self.repo.count, 0)
        self.assertEqual(self.repo.cards, [])

    def test_add__raises_exception(self):
        card = TrapCard('dragon')
        self.repo.add(card)
        self.assertEqual(self.repo.count, 1)
        card2 = MagicCard('dragon')
        with self.assertRaises(ValueError) as exc:
            self.repo.add(card2)
        self.assertEqual(str(exc.exception), "Card dragon already exists!")

    def test_add(self):
        card = TrapCard('dragon')
        self.repo.add(card)
        self.assertEqual(self.repo.count, 1)
        self.assertIn(card, self.repo.cards)

    def test_remove__raises_exception(self):
        with self.assertRaises(ValueError) as exc:
            self.repo.remove('')
        self.assertEqual(str(exc.exception), "Card cannot be an empty string!")

    def test_remove(self):
        card = TrapCard('dragon')
        self.repo.add(card)
        self.assertEqual(self.repo.count, 1)
        self.repo.remove('dragon')
        self.assertEqual(self.repo.count, 0)
        self.assertEqual(self.repo.cards, [])

    def test_find(self):
        card = TrapCard('dragon')
        card2 = MagicCard('drake')
        self.repo.add(card)
        self.repo.add(card2)
        result = self.repo.find('drake')
        self.assertEqual(result, card2)


if __name__ == '__main__':
    unittest.main()
