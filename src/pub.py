from jinja2 import pass_environment


class Pub:
    # Constructor
    def __init__(self, _name, _till):
        self.name = _name
        self.till = _till

    def age_check(self, customer):
        if customer.age >= 18:
            return True
        else:
            return False

    def increase_till(self, amount):
        self.till += amount

    def drunkness_check(self, customer):
        if customer.drunkness <= 10:
            return True
        else:
            return False

    def sell_drink(self, drink, customer):
        if self.age_check(customer) and self.drunkness_check(customer):
            customer.reduce_wallet(drink.price)
            self.increase_till(drink.price)
