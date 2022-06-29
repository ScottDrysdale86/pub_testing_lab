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
