import random

from random import randint

class BankAccount:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.balance = balance
        balance = 0
        self.account_number = str(account_number)
        self.account_number = "*" * 4 + self.account_number[4:]

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

    def add_interest(self, rate=0.00083):
        interest = self.balance * rate
        self.balance += interest

    def print_statement(self):
        print(f"{self.name}\nAccount No.: {self.account_number}\nBalance: ${self.balance:.2f}")

john_BankAccount = BankAccount("John Augustus", 12345678, 1000)

john_BankAccount.print_statement()

amy_BankAccount = BankAccount("Amy Brooke", 79598828, 1500)

amy_BankAccount.get_balance()

james_BankAccount = BankAccount("James Mizutani", 60716208, 3400)

james_BankAccount.withdraw(3500)

mitchell_BankAccount = BankAccount("Mitchell", "03141592", 10000)
'''
mitchell_BankAccount.print_statement()

mitchell_BankAccount.deposit(400000)
'''
mitchell_BankAccount.print_statement()

mitchell_BankAccount.add_interest()


