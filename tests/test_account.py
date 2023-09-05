import unittest

from lib.account import Account

class Bank_Account_Test(unittest.TestCase):

    def setUp(self):
        self.account = Account()
       

    def test_default_balance(self):
        self.assertEqual(self.account.balance, 0)