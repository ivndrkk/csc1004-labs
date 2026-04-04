class BankAccount:
    def __init__(self,balance=0):
        self.balance = float(balance)
    def deposit(self, amount):
        if amount > 0:
            self.balance += float(amount)
    def withdraw(self,amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= float(amount)
    def __str__(self):
        return f"Your current balance is {self.balance:.2f} euro"