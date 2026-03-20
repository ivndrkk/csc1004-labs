class BankAccount:
    def __init__(self, balance=0):
        self.balance = float(balance)
        self.history = []
        self.opening_balance = float(balance)

    def deposit(self, amount):
        self.balance += amount
        self.history.append(f"{amount:.2f} deposit for a new balance of {self.balance:.2f}")
        if len(self.history) > 3:
            self.history.pop(0)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.history.append(f"-{amount:.2f} withdrawal for a new balance of {self.balance:.2f}")
            if len(self.history) > 3:
                self.history.pop(0)

    def __str__(self):
        lines = [f"Opening balance: {self.opening_balance:.2f} euros"]
        lines.extend(self.history)
        lines.append(f"Current balance: {self.balance:.2f} euros")
        return '\n'.join(lines)
