# Create a class called BankAccount with the following private attributes:

# account_number (string or int)

# account_holder_name (string)

# balance (float)

# 2. Provide public methods to:

# Set account details (account_number, account_holder_name)

# Deposit money

# Withdraw money (only if balance is sufficient)

# Get the current balance

# Display account information (account number, holder name, and balance)

# 3. Ensure proper validation:

# Balance cannot be set or become negative.

# Account number and holder name must be non-empty.

# Deposits and withdrawals must be positive amounts.

# 4. Bonus (Optional):

# Add a transaction history list that logs every deposit and withdrawal.

# Add a method to print the transaction history.

# ✅ Expected Outcome:

# You should be able to:

# Create an account

# Deposit and withdraw money

# View account details

# Ensure data safety through encapsulation (no direct access to sensitive fields)

class BankAccount:
    def __init__(self):
        self.__account_number = None
        self.__account_holder_name = None
        self.__balance = 0.0
        self.__transaction_history = []

    # Set account details
    def set_account_details(self, account_number, account_holder_name):
        if not account_number or not account_holder_name:
            print("Account number and holder name cannot be empty.")
            return

        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        print("Account created successfully.")

    # Deposit money
    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return

        self.__balance += amount
        self.__transaction_history.append(f"Deposited: ${amount:.2f}")
        print(f"Deposited ${amount:.2f} successfully.")

    # Withdraw money
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return

        if amount > self.__balance:
            print("Insufficient balance.")
            return

        self.__balance -= amount
        self.__transaction_history.append(f"Withdrew: ${amount:.2f}")
        print(f"Withdrew ${amount:.2f} successfully.")

    def get_balance(self):
        return self.__balance

    def display_account_info(self):
        print("\n--- Account Information ---")
        print(f"Account Number: {self.__account_number}")
        print(f"Account Holder: {self.__account_holder_name}")
        print(f"Balance: ${self.__balance:.2f}")
        print("-----------------------------")

    def print_transaction_history(self):
        print("\n--- Transaction History ---")
        if not self.__transaction_history:
            print("No transactions yet.")
        else:
            for transaction in self.__transaction_history:
                print(transaction)
        print("---------------------------")

if __name__ == "__main__":
    account = BankAccount()

    account.set_account_details("ABC123456", "Alice Johnson")
    account.deposit(1000)
    account.withdraw(250)
    account.deposit(500)
    account.withdraw(1500)  

    print(f"\nCurrent Balance: ${account.get_balance():.2f}")
    account.display_account_info()
    account.print_transaction_history()
