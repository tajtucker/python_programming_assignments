import numpy as np

class Account:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self, amount):
        if amount < 0:
            print("Error: Deposit amount must be positive.")
            return
        else:
            self.balance += amount
    
    def withdraw(self, amount):
        if amount < 0:
            print("Error: Withdrawal amount must be positive.")
            return
        elif amount > self.balance:
            print("Error: Withdrawal amount exceeds balance.")
            return
        else:
            self.balance -= amount
        
    def display_details(self):
        print(self.account_number)
        print(self.account_holder)
        print(self.balance)
    

class SavingsAccount(Account):
    def __init__(self, account_number, account_holder, balance, interest_rate):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate
    
    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest

        print(f"Interest Applied: {interest}")
        print(f"New Balance: {self.balance}")

acc1 = SavingsAccount(1001, "Chris", 4500, .10)
acc2 = SavingsAccount(1002, "John", 2300, .10)
acc3 = SavingsAccount(1003, "Amber", 10000, .10)

arr = np.array([acc1, acc2, acc3])

print("Account details initially:\n")
for i in arr:
    i.display_details()
    print()

for i in arr:
    i.apply_interest()
    print()

print("Account details after interest:\n")
for i in arr:
    i.display_details()
    print()