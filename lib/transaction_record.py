from datetime import datetime

class Transaction_Record:

    def __init__(self, date = datetime.today().strftime('%d-%m-%Y'), credit = None, debit = None, balance = None):
        self.date = date
        self.credit = credit
        self.debit = debit
        self.balance = balance