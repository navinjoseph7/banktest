import pytest
import unittest
from unittest import mock
from lib.transaction import Transaction

class Transaction_Test(unittest.TestCase):

    def setUp(self):
        self.transaction = Transaction()
        self.transaction.transaction_record = mock.Mock(name="transaction_record")
        self.transaction.history.clear()

    def test_credit(self):
        self.transaction.credit(0, 10)
        self.transaction.transaction_record.assert_called_once_with(balance=10, credit=10)
        self.assertEqual(len(self.transaction.history), 1)

    def test_debit(self):
        self.transaction.debit(10, 5)
        self.transaction.transaction_record.assert_called_once_with(balance=5, debit=5)
        self.assertEqual(len(self.transaction.history), 1)