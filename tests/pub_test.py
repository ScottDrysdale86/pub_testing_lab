import unittest
from src.pub import Pub
from src.customer import Customer


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