import unittest
from src.drink import Drink


class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink = Drink("Guinness", 1.00, 3)

    def test_drink_has_name(self):
        self.assertEqual("Guinness", self.drink.name)

    def test_drink_has_price(self):
        self.assertEqual(1.00, self.drink.price)

    def test_drink_has_alcohol_level(self):
        self.assertEqual(3, self.drink.alcohol_level)