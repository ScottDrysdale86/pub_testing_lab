class Customer:
    # Constructor
    def __init__(self, _name, _wallet, _age):
        self.name = _name
        self.wallet = _wallet
        self.age = _age
        self.drunkness = 0

    def increase_drunkness(self, amount):
        self.drunkness += amount