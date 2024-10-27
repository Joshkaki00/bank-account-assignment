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
        self.route_number = str(route_number) if route_number else str(random.randint(10000000, 99999999))
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

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name, account_number=None, route_number=None, balance=0, account_type="checking"):
        account = BankAccount(name, account_number, route_number, balance, account_type)
        self.accounts[account.account_number] = account
        print(f"Account created for {name} with account number {account.account_number}.")
        return account
    
    def deposit(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            account.deposit(amount)
        else:
            print("Account not found.")

    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            account.withdraw(amount)
        else:
            print("Account not found.")

    def transfer(self, from_account_number, to_account_number, amount):
        from_account = self.accounts.get(from_account_number)
        to_account = self.accounts.get(to_account_number)

        if from_account and to_account:
            if from_account.balance >= amount:
                from_account.withdraw(amount)
                to_account.deposit(amount)
                print(f"Transferred ${amount:.2f} from {from_account_number} to {to_account_number}." )
            else:
                print("Insufficient funds for transfer.")
        else:
            print("One or both accounts not found.")

    def statement(self, account_number)


def application():
    bank = {}

    while True:
        action = input("\nChoose an action: 'create account', 'statement', 'deposit', 'withdraw', or 'exit': ").strip().lower()

        if action == 'create account':
            name = input("Enter account holder's name: ")
            account_number = input("Enter account number (or press Enter to auto-generate): ").strip() or None
            route_number = input("Enter routing number (or press Enter to auto-generate): ").strip() or None
            balance = float(input("Enter initial balance: "))
            account_type = input("Enter account type ('savings' or 'checking'): ").strip().lower()

            new_account = BankAccount(name, account_number, route_number, balance, account_type)
            bank[new_account.account_number] = new_account
            print(f"Account created for {name} with account number {new_account.account_number}.")
        elif action == 'statement':
            account_number = input("Enter account number: ").strip()
            account = bank.get(account_number)
            if account:
                account.print_statement()
            else:
                print("Account not found.")

        elif action == 'deposit':
            account_number = input("Enter account number: ").strip()
            account = bank.get(account_number)
            if account:
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)
            else:
                print("Account not found.")

        elif action == 'withdraw':
            account_number = input("Enter account number: ").strip()
            account = bank.get(account_number)
            if account:
                amount = float(input("Enter amount to withdraw: "))
                account.withdraw(amount)
            else:
                print("Account not found.")

        elif action == 'exit':
            print("Thank you for banking with us.")
            break

        else:
            print("Invalid action. Please choose a valid action.")

application()