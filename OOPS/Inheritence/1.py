# Parent Class
class BankAccount:
    def __init__(self, account_no, name, balance):
        self.account_no = account_no
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Amount Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount Withdrawn:", amount)
        else:
            print("Insufficient Balance")

    def show_balance(self):
        print("Current Balance:", self.balance)


# Child Class 1
class SavingsAccount(BankAccount):
    def __init__(self, account_no, name, balance, interest_rate):
        super().__init__(account_no, name, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = (self.balance * self.interest_rate) / 100
        self.balance += interest
        print("Interest Added:", interest)


# Child Class 2
class CurrentAccount(BankAccount):
    def __init__(self, account_no, name, balance, overdraft_limit):
        super().__init__(account_no, name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print("Amount Withdrawn:", amount)
        else:
            print("Overdraft Limit Exceeded")


# Main Program
print("---- Savings Account ----")
s = SavingsAccount(101, "Shalini", 5000, 5)
s.deposit(1000)
s.withdraw(2000)
s.add_interest()
s.show_balance()

print("\n---- Current Account ----")
c = CurrentAccount(102, "Rahul", 3000, 2000)
c.withdraw(4500)
c.show_balance()
