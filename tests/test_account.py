import unittest

from lib.account import Account

class Bank_Account_Test(unittest.TestCase):

    def setUp(self):
        self.account = Account()
       

    def test_default_balance(self):
        self.assertEqual(self.account.balance, 0)

    def test_deposit(self):
        self.account.deposit(500)
        assert self.account.balance == 500
    
    def test_withdraw(self):
        self.account.deposit(500)
        self.account.withdraw(200)
        assert self.account.balance == 300