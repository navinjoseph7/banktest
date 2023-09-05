class Account:
    def __init__(self, balance=0):
        self.balance = 0
    def deposit(self, amount):
        self.balance += amount
        