from datetime import datetime

class Transaction_Record:

    def __init__(self, date = datetime.today().strftime('%d-%m-%Y'), credit = None, debit = None, balance = None):
        self.date = date
        self.credit = credit
        self.debit = debit
        self.balance = balance
    
    def __str__(self):
        if self.credit is not None:
            return f"{self.date} || {self.credit:.2f} || || {self.balance:.2f}"
        elif self.debit is not None:
            return f"{self.date} || || {self.debit:.2f} || {self.balance:.2f}"
        else:
            return f"{self.date} || || || {self.balance:.2f}"