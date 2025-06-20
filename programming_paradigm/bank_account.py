class BankAccount:
    def __init__(self, account_balance=None):
        if account_balance is not None:
            self.account_balance = account_balance
        else:
            self.account_balance = 0
    def deposit(self, amount):
        self.account_balance += amount
    def withdraw(self, amount):
        if (self.account_balance >= amount):
            self.account_balance -= amount
            return True
        return False
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance}.00")
