import unittest
from lib.transaction_record import Transaction_Record

class Transaction_Record_Test(unittest.TestCase):

    def setUp(self):
        self.credit_record = Transaction_Record(date = "01-04-2021", credit = 10, debit = None, balance = 10)
        self.withdraw_record = Transaction_Record(date = "01-04-2021", credit = None, debit = 10, balance = 0)

    def test_date(self):
        self.assertEqual(self.credit_record.date, '01-04-2021')
        self.assertEqual(self.withdraw_record.date, '01-04-2021')

    def test_credit(self):
        self.assertEqual(self.credit_record.credit, 10)
        self.assertEqual(self.withdraw_record.credit, None)

    def test_debit(self):
        self.assertEqual(self.credit_record.debit, None)
        self.assertEqual(self.withdraw_record.debit, 10)
