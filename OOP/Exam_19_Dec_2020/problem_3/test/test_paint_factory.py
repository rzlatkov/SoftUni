import unittest

from project.factory.paint_factory import PaintFactory


class TestPaintFactory(unittest.TestCase):
    def setUp(self):
        self.pf = PaintFactory('j', 1)

    def test_init(self):
        self.assertEqual(self.pf.name, 'j')
        self.assertEqual(self.pf.capacity, 1)
        self.assertEqual(self.pf.valid_ingredients, ["white", "yellow", "blue", "green", "red"])
        self.assertEqual(self.pf.ingredients, {})

    def test_add_ingredient__ingredient_not_valid(self):
        with self.assertRaises(TypeError) as exc:
            self.pf.add_ingredient('levski', 10)
        self.assertEqual(str(exc.exception), 'Ingredient of type levski not allowed in PaintFactory')

    def test_add_ingredient__no_space(self):
        with self.assertRaises(ValueError) as exc:
            self.pf.add_ingredient('white', 10)
        self.assertEqual(str(exc.exception), 'Not enough space in factory')

    def test_add_ingredient__ingredient_not_in_dict(self):
        self.pf.ingredients = {'red': 5, 'blue': 2}
        self.pf.add_ingredient('white', 1)
        self.assertEqual(self.pf.ingredients['white'], 1)

    def test_add_ingredient(self):
        self.pf.ingredients['white'] = 1
        self.pf.add_ingredient('white', 1)
        self.assertEqual(self.pf.ingredients['white'], 2)

    def test_remove_ingredient__ingredient_not_in_dict(self):
        with self.assertRaises(KeyError) as exc:
            self.pf.remove_ingredient('white', 1)
        self.assertEqual(str(exc.exception), '\'No such ingredient in the factory\'')

    def test_remove_ingredient__quantity_too_big(self):
        self.pf.ingredients['white'] = 5
        with self.assertRaises(ValueError) as exc:
            self.pf.remove_ingredient('white', 10)
        self.assertEqual(str(exc.exception), 'Ingredients quantity cannot be less than zero')

    def test_remove_ingredient(self):
        self.pf.ingredients['white'] = 10
        self.pf.remove_ingredient('white', 6)
        self.assertEqual(self.pf.ingredients['white'], 4)

    def test_products_property(self):
        self.pf.ingredients = {'red': 5, 'blue': 2}
        result = self.pf.products
        self.assertEqual(self.pf.ingredients, result)


if __name__ == '__main__':
    unittest.main()
