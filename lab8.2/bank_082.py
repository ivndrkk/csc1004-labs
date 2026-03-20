class BankAccount:
    def __init__(self, balance=0):
        self.balance = float(balance)

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount

    def __str__(self):
        return f"Your current balance is {self.balance:.2f} euro"
