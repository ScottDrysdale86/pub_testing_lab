import unittest
from src.customer import Customer


class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Scott", 50.00, 20)

    def test_customer_has_name(self):
        self.assertEqual("Scott", self.customer.name)

    def test_customer_has_wallet(self):
        self.assertEqual(50.00, self.customer.wallet)

    def test_customer_has_age(self):
        self.assertEqual(20, self.customer.age)

    def test_customer_has_drunkness(self):
        self.assertEqual(0, self.customer.drunkness)

    def test_increase_drunkness(self):
        self.customer.increase_drunkness(3)
        self.assertEqual(3, self.customer.drunkness)

    def test_reduce_wallet(self):
        self.customer.reduce_wallet(3.00)
        self.assertEqual(47.00, self.customer.wallet)
