import unittest
from src.food import Food


class TestFood(unittest.TestCase):
    def setUp(self):
        self.food = Food("Burger", 3.99, 3)

    def test_food_has_name(self):
        self.assertEqual("Burger", self.food.name)

    def test_food_has_price(self):
        self.assertEqual(3.99, self.food.price)

    def test_food_has_rejuvenation_level(self):
        self.assertEqual(3, self.food.rejuvenation_level)