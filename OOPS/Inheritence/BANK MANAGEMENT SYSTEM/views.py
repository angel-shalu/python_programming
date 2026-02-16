class BankAccount:
    def __init__(self, acc_no, name, pin, balance=0):
        self.acc_no = acc_no
        self.name = name
        self.pin = pin
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited ₹{amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrawn ₹{amount}")
            return True
        return False


class SavingsAccount(BankAccount):
    def __init__(self, acc_no, name, pin, balance, interest_rate):
        super().__init__(acc_no, name, pin, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        self.transactions.append(f"Interest Added ₹{interest}")


class CurrentAccount(BankAccount):
    def __init__(self, acc_no, name, pin, balance, overdraft_limit):
        super().__init__(acc_no, name, pin, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            self.transactions.append(f"Withdrawn ₹{amount} (Overdraft)")
            return True
        return False
