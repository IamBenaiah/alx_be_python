class BankAccount:
    """A simple bank account class to handle deposits and withdrawals."""

    def __init__(self, initial_balance=0.0):
        """Initialize the account with an optional starting balance."""
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Deposit a given amount to the account."""
        if amount > 0:
            self.account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw a given amount if funds are sufficient."""
        if 0 < amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            print("Insufficient funds or invalid amount.")
            return False

    def display_balance(self):
        """Display the current account balance."""
        print(f"Current Balance: ${self.account_balance:.2f}")
