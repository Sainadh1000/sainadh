# Class: BankAccount

# Attributes:

# account_holder (str)

# balance (float)

# Methods:

# deposit(amount)

# withdraw(amount)

# display_balance()

# Class: SavingsAccount (inherits from BankAccount)

# Attribute:

# interest_rate (float)

# Method:

# add_interest() → adds interest to balance

# Class: CurrentAccount (inherits from BankAccount)

# Attribute:

# overdraft_limit (float)

# Override withdraw() to allow withdrawal beyond balance up to the overdraft limit

# Demonstrate by:

# Creating both types of accounts

# Making deposits, withdrawals

# Showing how SavingsAccount adds interest

# Showing how CurrentAccount handles overdraft

class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance: {self.balance}")

    def display_balance(self):
        print(f"Balance for {self.account_holder}: {self.balance}")


class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance=0, interest_rate=0.02):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest of {interest} added. New balance: {self.balance}")


class CurrentAccount(BankAccount):
    def __init__(self, account_holder, balance=0, overdraft_limit=500):
        super().__init__(account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > self.balance + self.overdraft_limit:
            print("Overdraft limit exceeded!")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance: {self.balance}")

savings = SavingsAccount("Alice", 1000, interest_rate=0.05)
current = CurrentAccount("Bob", 500, overdraft_limit=300)


savings.deposit(200)
savings.add_interest()
savings.withdraw(100)
savings.display_balance()

print("-"*50)

current.withdraw(600) 
current.withdraw(300)  
current.deposit(500)
current.display_balance()