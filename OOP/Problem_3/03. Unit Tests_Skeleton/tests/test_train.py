import unittest

from project.train.train import Train


class TestTrain(unittest.TestCase):
    # def setUp(self):
    #     self.train = Train('fast', 10)

    def test_init(self):
        self.train = Train('fast', 10)

        self.assertEqual(self.train.name, 'fast')
        self.assertEqual(self.train.capacity, 10)
        self.assertEqual(self.train.passengers, [])

    def test_add__raises_train_full(self):
        self.train = Train('fast', 1)
        self.train.add('john')
        # self.assertEqual(self.train.passengers[0], 'john')
        with self.assertRaises(ValueError) as exc:
            self.train.add('joe')
        self.assertEqual(str(exc.exception), "Train is full")

    def test_add__raises_passenger_exists(self):
        self.train = Train('fast', 5)
        self.train.add('john')
        with self.assertRaises(ValueError) as exc:
            self.train.add('john')
        self.assertEqual(str(exc.exception), "Passenger john Exists")

    def test_add_okay(self):
        self.train = Train('fast', 5)
        res = self.train.add('john')
        self.assertEqual(res, "Added passenger john")

    def test_remove__raises_passenger_not_found(self):
        self.train = Train('fast', 5)
        self.train.add('john')
        with self.assertRaises(ValueError) as exc:
            self.train.remove('jack')
        self.assertEqual(str(exc.exception), "Passenger Not Found")

    def test_remove_okay(self):
        self.train = Train('fast', 5)
        self.train.add('john')
        self.train.add('jack')
        res = self.train.remove('john')
        self.assertEqual(res, "Removed john")


if __name__ == '__main__':
    unittest.main()
