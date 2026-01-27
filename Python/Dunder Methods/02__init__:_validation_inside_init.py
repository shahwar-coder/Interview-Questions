'''
TASK 2: VALIDATION INSIDE __init__

Write a class `Account` with an __init__ method that:
- Accepts `balance`
- Raises ValueError if balance is negative
- Stores the balance only if it is valid
- Create one valid object and attempt to create one invalid object

RULES:
- Perform validation inside __init__
- Do NOT modify attributes after object creation

GOAL:
Understand how __init__ prepares an object
and prevents invalid state at creation time.
'''

class Account:
    def __init__(self, balance):
        if balance<0:
            raise ValueError("Balance can not be negative")
        self.balance = balance

    
# Valid account
account1 = Account(14000)
print(f"Acc Balance:\n"
      f"{account1.balance}")
# Acc Balance:
# 14000


try:
    account2 = Account(-500)
except ValueError as err:
    print(f"Error creaing account: {err}")

# Error creaing account: Balance can not be negative