import unittest
from src.pub import Pub
from src.customer import Customer
from src.drink import Drink
from src.food import Food


class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00)
        self.pub1 = Pub("Bannermans", 200.00)

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(100.00, self.pub.till)

    def test_age_legal(self):
        customer = Customer("Scott", 50.00, 20)
        age = self.pub.age_check(customer)
        self.assertEqual(True, age)

    def test_age_not_legal(self):
        customer = Customer("Scott", 50.00, 16)
        age = self.pub.age_check(customer)
        self.assertEqual(False, age)

    def test_till_increase(self):
        self.pub.increase_till(3.00)
        self.assertEqual(103.00, self.pub.till)

    def test_drunkness_ok(self):
        customer = Customer("Scott", 50.00, 20)
        drunkness = self.pub.drunkness_check(customer)
        self.assertEqual(True, drunkness)

    def test_drunkness__not_ok(self):
        customer = Customer("Scott", 50.00, 20)
        customer.increase_drunkness(20)
        drunkness = self.pub.drunkness_check(customer)
        self.assertEqual(False, drunkness)

    def test_sell_drink_ok(self):
        customer = Customer("Scott", 50.00, 20)
        drink = Drink("Guinness", 1, 11)
        self.assertEqual(True, self.pub.age_check(customer))
        self.assertEqual(True, self.pub.drunkness_check(customer))
        self.pub.sell_drink(drink, customer)
        self.assertEqual(49.00, customer.wallet)
        self.assertEqual(101.00, self.pub.till)
        self.assertEqual(11, customer.drunkness)

    def test_sell_drink_underage(self):
        customer = Customer("Stuart", 20.00, 17)
        drink = Drink("Guinness", 1, 11)
        self.assertEqual(False, self.pub.age_check(customer))
        self.assertEqual(True, self.pub.drunkness_check(customer))
        self.pub.sell_drink(drink, customer)
        self.assertEqual(20.00, customer.wallet)
        self.assertEqual(100.00, self.pub.till)
        self.assertEqual(0, customer.drunkness)

    def test_sell_drink_too_drunk(self):
        customer = Customer("Stuart", 20.00, 18)
        drink = Drink("Guinness", 1, 11)
        self.assertEqual(True, self.pub.age_check(customer))
        self.assertEqual(True, self.pub.drunkness_check(customer))
        self.pub.sell_drink(drink, customer)
        self.assertEqual(19.00, customer.wallet)
        self.assertEqual(101.00, self.pub.till)
        self.assertEqual(11, customer.drunkness)

        self.assertEqual(True, self.pub.age_check(customer))
        self.assertEqual(False, self.pub.drunkness_check(customer))
        self.pub.sell_drink(drink, customer)
        self.assertEqual(19.00, customer.wallet)
        self.assertEqual(101.00, self.pub.till)
        self.assertEqual(11, customer.drunkness)

    def test_sell_food(self):
        customer = Customer("Scott", 50.00, 20)
        food = Food("Burger", 3.99, 3)
        self.pub.sell_food(food, customer)
        self.assertEqual(46.01, customer.wallet)
        self.assertEqual(103.99, self.pub.till)
        self.assertEqual(-3, customer.drunkness)

    def test_quantity_check(self):
        drink = self.pub.check_quantity("Guinness")
        self.assertEqual(5, self.pub.check_quantity("Guinness"))

    def test_reduce_quantity(self):
        drink = Drink("Guinness", 1, 11)
        self.pub.reduce_quantity("Guinness")
        self.assertEqual(4, self.pub.check_quantity(drink.name))

    def test_stock_value(self):
        drink = Drink("Guinness", 1, 5)
        drink2 = Drink("Corona", 2, 5)
        drink_list = [drink, drink2]
        self.assertEqual(7.00, self.pub.stock_value(drink_list))
