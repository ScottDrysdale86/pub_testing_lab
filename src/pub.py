class Pub:
    # Constructor
    def __init__(self, _name, _till):
        self.name = _name
        self.till = _till
        self.drinks = {"Guinness": 5, "Corona": 1}

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
        if (
            self.age_check(customer)
            and self.drunkness_check(customer)
            and self.check_quantity(drink.name) > 0
        ):
            customer.reduce_wallet(drink.price)
            self.increase_till(drink.price)
            customer.increase_drunkness(drink.alcohol_level)
            self.reduce_quantity(drink.name)

    def sell_food(self, food, customer):
        customer.reduce_wallet(food.price)
        self.increase_till(food.price)
        customer.reduce_drunkness(food.rejuvenation_level)

    def check_quantity(self, drink_name):
        return self.drinks[drink_name]

    def reduce_quantity(self, drink):
        self.drinks[drink] -= 1

    def stock_value(self, drinks_list):
        total_value = 0
        for drink in self.drinks:
            for name in drinks_list:
                if drink == name.name:
                    total_value += self.drinks[drink] * name.price
        return total_value
