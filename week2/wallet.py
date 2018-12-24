class InsufficientAmount(Exception):
    pass


class Wallet:

    def __init__(self, balance=0):
        self.balance = balance

    def spend_cash(self, amount):
        if self.balance < amount:
            raise InsufficientAmount(
                'Not enough available to spend {}'.format(amount))
        self.balance -= amount

    def add_cash(self, amount):
        self.balance += amount

    def info(self):
        return "Your wallet has {}".format(self.balance)
