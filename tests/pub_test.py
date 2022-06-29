import unittest
from src.pub import Pub
from src.customer import Customer
from src.drink import Drink
from src.food import Food


class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)
        self.pub1 = Pub("Bannermans", 200.00)
        self.customer = Customer("Scott", 50.00, 20)
        self.customer2 = Customer("Stuart", 20.00, 17)
        self.customer3 = Customer("Stuart", 1.00, 18)
        self.drink = Drink("Guinness", 1, 11)
        self.drink2 = Drink("Guinness", 1, 5)
        self.drink3 = Drink("Corona", 2, 5)
        self.food = Food("Burger", 3.99, 3)

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(100.00, self.pub.till)

    def test_age_legal(self):
        age = self.pub.age_check(self.customer)
        self.assertEqual(True, age)

    def test_age_not_legal(self):
        age = self.pub.age_check(self.customer2)
        self.assertEqual(False, age)

    def test_till_increase(self):
        self.pub.increase_till(3.00)
        self.assertEqual(103.00, self.pub.till)

    def test_drunkness_ok(self):
        drunkness = self.pub.drunkness_check(self.customer)
        self.assertEqual(True, drunkness)

    def test_drunkness__not_ok(self):
        self.customer.increase_drunkness(20)
        drunkness = self.pub.drunkness_check(self.customer)
        self.assertEqual(False, drunkness)

    def test_sell_drink_ok(self):
        self.assertEqual(True, self.pub.age_check(self.customer))
        self.assertEqual(True, self.pub.drunkness_check(self.customer))
        self.pub.sell_drink(self.drink, self.customer)
        self.assertEqual(49.00, self.customer.wallet)
        self.assertEqual(101.00, self.pub.till)
        self.assertEqual(11, self.customer.drunkness)

    def test_sell_drink_underage(self):
        self.assertEqual(False, self.pub.age_check(self.customer2))
        self.assertEqual(True, self.pub.drunkness_check(self.customer2))
        self.pub.sell_drink(self.drink, self.customer2)
        self.assertEqual(20.00, self.customer2.wallet)
        self.assertEqual(100.00, self.pub.till)
        self.assertEqual(0, self.customer2.drunkness)

    def test_sell_drink_too_drunk(self):
        self.assertEqual(True, self.pub.age_check(self.customer))
        self.assertEqual(True, self.pub.drunkness_check(self.customer))

        self.pub.sell_drink(self.drink, self.customer)
        self.assertEqual(49.00, self.customer.wallet)
        self.assertEqual(101.00, self.pub.till)
        self.assertEqual(11, self.customer.drunkness)

        self.assertEqual(True, self.pub.age_check(self.customer))
        self.assertEqual(False, self.pub.drunkness_check(self.customer))
        self.pub.sell_drink(self.drink, self.customer)
        self.assertEqual(49.00, self.customer.wallet)
        self.assertEqual(101.00, self.pub.till)
        self.assertEqual(11, self.customer.drunkness)

    def test_sell_food(self):
        self.pub.sell_food(self.food, self.customer)
        self.assertEqual(46.01, self.customer.wallet)
        self.assertEqual(103.99, self.pub.till)
        self.assertEqual(-3, self.customer.drunkness)

    def test_quantity_check(self):
        drink = self.pub.check_quantity("Guinness")
        self.assertEqual(5, self.pub.check_quantity("Guinness"))

    def test_reduce_quantity(self):
        self.pub.reduce_quantity("Guinness")
        self.assertEqual(4, self.pub.check_quantity(self.drink.name))

    def test_stock_value(self):
        drink_list = [self.drink2, self.drink3]
        self.assertEqual(7.00, self.pub.stock_value(drink_list))

    def test_sufficient_funds(self):
        fund_check = self.pub.sufficient_funds(self.customer, self.drink3)
        self.assertEqual(True, fund_check)

    def test_insufficient_funds(self):
        fund_check = self.pub.sufficient_funds(self.customer3, self.drink3)
        self.assertEqual(False, fund_check)
