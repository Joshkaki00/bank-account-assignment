import random

from random import randint

class BankAccount:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance
        balance = 0
        self.account_number = str(account_number)
        self.account_number = self.account_number[:5] + "*" * 3

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
        print(f"Your current balance is : {self.balance:.2f}")

    def add_interest(self, rate):
        interest = self.balance * rate
        self.rate = 0.00083
        self.balance += interest

    def print_statement(self):
        print(f"{self.name}\nAccount No.: {self.account_number}\nBalance: ${self.balance:.2f}")

john_BankAccount = BankAccount("John", 12345678, 1000)

john_BankAccount.deposit(500)

john_BankAccount.withdraw(250)

john_BankAccount.get_balance()

john_BankAccount.add_interest()

john_BankAccount.print_statement()

amy_BankAccount = BankAccount

