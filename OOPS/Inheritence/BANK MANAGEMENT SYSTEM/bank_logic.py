# ================= PARENT CLASS =================
class BankAccount:
    def __init__(self, acc_no, name, pin, balance=0):
        self.acc_no = acc_no
        self.name = name
        self.__pin = pin          # Encapsulation
        self.balance = balance
        self.transactions = []

    def verify_pin(self, pin):
        return self.__pin == pin

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited ₹{amount}")
        print("Deposit successful")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrawn ₹{amount}")
            print("Withdrawal successful")
        else:
            print("Insufficient balance")

    def check_balance(self):
        print(f"Available Balance: ₹{self.balance}")

    def show_transactions(self):
        print("\nTransaction History:")
        for t in self.transactions:
            print("-", t)

    def account_details(self):
        print("\nAccount Details")
        print("Account No:", self.acc_no)
        print("Holder Name:", self.name)
        print("Balance:", self.balance)


# ================= SAVINGS ACCOUNT =================
class SavingsAccount(BankAccount):
    def __init__(self, acc_no, name, pin, balance, interest_rate):
        super().__init__(acc_no, name, pin, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        self.transactions.append(f"Interest added ₹{interest}")
        print("Interest credited successfully")


# ================= CURRENT ACCOUNT =================
class CurrentAccount(BankAccount):
    def __init__(self, acc_no, name, pin, balance, overdraft_limit):
        super().__init__(acc_no, name, pin, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            self.transactions.append(f"Withdrawn ₹{amount} (Overdraft)")
            print("Withdrawal successful (Overdraft used)")
        else:
            print("Overdraft limit exceeded")


# ================= MAIN PROGRAM =================
print("🏦 Welcome to Bank Management System")

print("\nChoose Account Type")
print("1. Savings Account")
print("2. Current Account")
choice = int(input("Enter choice: "))

acc_no = int(input("Enter Account Number: "))
name = input("Enter Account Holder Name: ")
pin = int(input("Set 4-digit PIN: "))
balance = float(input("Enter Initial Balance: "))

if choice == 1:
    rate = float(input("Enter Interest Rate (%): "))
    account = SavingsAccount(acc_no, name, pin, balance, rate)
else:
    limit = float(input("Enter Overdraft Limit: "))
    account = CurrentAccount(acc_no, name, pin, balance, limit)

# ================= MENU =================
while True:
    print("""
    1. Deposit
    2. Withdraw
    3. Check Balance
    4. Transaction History
    5. Account Details
    6. Add Interest (Savings only)
    7. Exit
    """)

    option = int(input("Enter option: "))
    user_pin = int(input("Enter PIN: "))

    if not account.verify_pin(user_pin):
        print("Invalid PIN")
        continue

    if option == 1:
        amt = float(input("Enter amount: "))
        account.deposit(amt)

    elif option == 2:
        amt = float(input("Enter amount: "))
        account.withdraw(amt)

    elif option == 3:
        account.check_balance()

    elif option == 4:
        account.show_transactions()

    elif option == 5:
        account.account_details()

    elif option == 6:
        if isinstance(account, SavingsAccount):
            account.add_interest()
        else:
            print("Interest not applicable for Current Account")

    elif option == 7:
        print("Thank you for using our Bank")
        break

    else:
        print("Invalid choice")
