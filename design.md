USER STORY
------------
As an account holder,
I should be able to see balance,
So I can know my balance

As an account holder,
I should be able to deposit money

As an account holder,
I should be able to withdraw money

As an account holder,
I should be able to see transaction history of my account with date

DESIGN OF CLASSES
--------------------
ACCOUNT Class : deposit and withdraw functions , depends on TRANSACTION class
TRANSACTION Class : credit () to deposit money , debit () to withdraw money , transaction_history () to save the transaction details
TRANSACTION RECORD Class : saves the ttransaction history in correct format

