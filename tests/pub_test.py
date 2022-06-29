import unittest
from src.pub import Pub
from src.customer import Customer
from src.drink import Drink


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

    def test_sell_drink(self):
        customer = Customer("Scott", 50.00, 20)
        customer2 = Customer("Stuart", 20.00, 17)
        drink = Drink("Guinness", 1, 11)
        self.pub.sell_drink(drink, customer)
        self.assertEqual(True, self.pub.age_check(customer))
        self.assertEqual(True, self.pub.drunkness_check(customer))
        self.assertEqual(49.00, customer.wallet)
        self.assertEqual(101.00, self.pub.till)
