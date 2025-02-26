class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize account balance with an optional initial value (default is 0)."""
        self.__account_balance = initial_balance

    def deposit(self, amount):
        """Deposit a specified amount into the account."""
        if amount > 0:
            self.__account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw a specified amount if sufficient funds are available."""
        if amount > 0 and amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """Print the current balance."""
        print(f"Current Balance: ${self.__account_balance}")
