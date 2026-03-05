import numpy as np

class Account:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = float(balance)

    def deposit(self, amount):
        amount = float(amount)
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount

    def withdraw(self, amount):
        amount = float(amount)
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print("Withdrawal amount cannot exceed the balance.")
            return
        self.balance -= amount

    def display_details(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Current Balance: ${self.balance:,.2f}")
        print("-" * 35)


class SavingsAccount(Account):
    def __init__(self, account_number, account_holder, balance, interest_rate):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = float(interest_rate)

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest applied to Account {self.account_number}: ${interest:,.2f}")
        print(f"New Balance: ${self.balance:,.2f}")
        print("-" * 35)



acc1 = SavingsAccount(1001, "Chris", 4500, 0.10)
acc2 = SavingsAccount(1002, "John", 2300, 0.10)
acc3 = SavingsAccount(1003, "Amber", 10000, 0.10)

accounts = np.array([acc1, acc2, acc3], dtype=object)

print("ACCOUNT DETAILS BEFORE APPLYING INTEREST")
print("=" * 35)
for acc in accounts:
    acc.display_details()

print("\nAPPLYING INTEREST")
print("=" * 35)
for acc in accounts:
    acc.apply_interest()

print("\nACCOUNT DETAILS AFTER APPLYING INTEREST")
print("=" * 35)
for acc in accounts:
    acc.display_details()