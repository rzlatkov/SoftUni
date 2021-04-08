import unittest

from project.appliances.fridge import Fridge
from project.appliances.tv import TV
from project.people.child import Child
from project.rooms.room import Room


class RoomTests(unittest.TestCase):
    def setUp(self):
        self.room = Room('joes', 500, 2)

    def test_init(self):
        self.assertEqual('joes', self.room.family_name)
        self.assertEqual(500, self.room.budget)
        self.assertEqual(2, self.room.members_count)
        self.assertEqual([], self.room.children)
        # self.assertTrue(hasattr(self.room, 'expenses'))
        self.assertEqual(0, self.room.expenses)

    def test_calculate_expenses_with_args(self):
        apps = [TV(), Fridge()]
        chlds = [Child(1, 2), Child(3, 4)]
        self.room.calculate_expenses(apps, chlds)
        self.assertEqual(self.room.expenses, 381)

    def test_calculate_expenses_no_args_expected_zero(self):
        self.room.calculate_expenses()
        self.assertEqual(self.room.expenses, 0)

    def test_expenses_negative_raises_ValueError(self):
        with self.assertRaises(ValueError) as exc:
            self.room.expenses = -1
        self.assertEqual(str(exc.exception), 'Expenses cannot be negative')

    def test_calculate_expenses_raises_TypeError(self):
        with self.assertRaises(TypeError) as exc:
            self.room.calculate_expenses(5)


if __name__ == '__main__':
    unittest.main()
