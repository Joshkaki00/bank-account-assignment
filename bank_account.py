import random

from random import randint

class BankAccount:
    def __init__(self, name, account_number, route_number, balance, account_type):
        self.name = name
        self.balance = balance
        balance = 0
        if account_number:
            self.account_number = str(account_number)
        else:
            self.account_number = str(random.randint(10000000, 99999999))
        self.account_number = "*" * 4 + self.account_number[4:]
        self.account_type = account_type
        if account_type == "savings":
            self.interest_rate = 0.001
        elif account_type == "checking":
            self.interest_rate = 0.00083
        else:
            raise ValueError("Invalid account type. Please enter \"savings\" or \"checking\".")
        self.route_number = route_number
        self.route_number = str(route_number)
        self.route_number = "0" * (9 - len(self.route_number)) + self.route_number

    

    def deposit(self, amount):
        self.balance += amount
        print(f"Amount deposited: ${amount:.2f} new balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
            self.balance -= 10
        else:
            self.balance -= amount
            print(f"Amount withdrawn: ${amount:.2f} new balance: ${self.balance:.2f}")

    def get_balance(self):
        print(f"Your current balance is : ${self.balance:.2f}")

    def add_interest(self, rate=None):
        interest = self.balance * self.interest_rate
        self.balance += interest

    def print_statement(self):
        print(f"{self.name}\nAccount No.: {self.account_number}\nRouting No.: {self.route_number}\nBalance: ${self.balance:.2f}\nAccount Type: {self.account_type.capitalize()}")



savings_account = BankAccount("John Augustus", 12345678, 987654325, 1000, "savings")

savings_account.deposit(500)

savings_account.print_statement()

checking_account = BankAccount("Ken Mizutani", None, 107846534, 2000, "checking")

checking_account.withdraw(2100)

checking_account = BankAccount("Mitchell", "03141592", 345678919, 0, "checking")

checking_account.deposit(400000)

checking_account.print_statement()

checking_account.add_interest()

checking_account.print_statement()

checking_account.withdraw(150)

checking_account.print_statement()

bank = [checking_account, savings_account]

def apply_interest_to_all_accounts(bank):
    for account in bank:
        account.add_interest()

apply_interest_to_all_accounts(bank)

for account in bank:
    account.print_statement()