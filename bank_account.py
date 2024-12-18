import random

# This is class BankAccount

class BankAccount:
    def __init__(self, full_name, account_number=None, route_number=None, balance=0, account_type="checking"):
        self.full_name = full_name
        self.balance = balance
        self.account_number = str(account_number) if account_number else str(random.randint(10000000, 99999999))
        self.display_account_number = "*" * 4 + self.account_number[4:]
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

# These are the methods for BankAccount

    def deposit(self, amount):
        self.balance += amount
        print(f"Amount deposited: ${amount:.2f}. New balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
            self.balance -= 10
        else:
            self.balance -= amount
            print(f"Amount withdrawn: ${amount:.2f}. New balance: ${self.balance:.2f}")

    def get_balance(self):
        print(f"Your current balance is : ${self.balance:.2f}")

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest

    def print_statement(self):
        print(f"{self.full_name}\nAccount No.: {self.display_account_number}\nRouting No.: {self.route_number}\nBalance: ${self.balance:.2f}\nAccount Type: {self.account_type.capitalize()}")

# Function called Bank that takes accounts and stores them

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name, account_number=None, route_number=None, balance=0, account_type="checking"):
        account = BankAccount(name, account_number, route_number, balance, account_type)
        self.accounts[account.account_number] = account
        print(f"Account created for {name} with account number {account.display_account_number}.")
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

    def add_interest(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            account.add_interest()
            print(f"Interest added to account {account.display_account_number}. New balance: ${account.balance:.2f}")
        else:
            print("Account not found.")

    def get_balance(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            account.get_balance()
        else:
            print("Account not found.")

    def transfer(self, from_account_number, to_account_number, amount):
        from_account = self.accounts.get(from_account_number)
        to_account = self.accounts.get(to_account_number)
        if from_account and to_account:
            if from_account.balance >= amount:
                from_account.withdraw(amount)
                to_account.deposit(amount)
                print(f"Transferred ${amount:.2f} from {from_account_number} to {to_account_number}.")
            else:
                print("Insufficient funds for transfer.")
        else:
            print("One or both accounts not found.")

    def statement(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            account.print_statement()
        else:
            print("Account not found.")

# Function called application that runs the program and UI

def application():
    bank = Bank()

    while True:
        action = input("\nChoose an action: 'create account', 'statement', 'deposit', 'withdraw', 'add interest', 'get balance', 'transfer', or 'exit': ").strip().lower()

        if action == 'create account':
            name = input("Enter account holder's name: ")
            account_number = input("Enter account number (or press Enter to auto-generate): ").strip() or None
            route_number = input("Enter routing number (or press Enter to auto-generate): ").strip() or None
            balance = float(input("Enter initial balance (numbers only, no currency symbol): "))
            account_type = input("Enter account type ('savings' or 'checking'): ").strip().lower()

            bank.create_account(name, account_number, route_number, balance, account_type)


        elif action == 'statement':
            account_number = input("Enter account number: ").strip()
            bank.statement(account_number)

        elif action == 'deposit':
            account_number = input("Enter account number: ").strip()
            amount = float(input("Enter amount to deposit (numbers only, no currency symbol): "))
            bank.deposit(account_number, amount)

        elif action == 'withdraw':
            account_number = input("Enter account number: ").strip()
            amount = float(input("Enter amount to withdraw (numbers only, no currency symbol): "))
            bank.withdraw(account_number, amount)

        elif action == 'add interest':
            account_number = input("Enter account number: ").strip()
            bank.add_interest(account_number)

        elif action == 'get balance':
            account_number = input("Enter account number: ").strip()
            bank.get_balance(account_number)

        elif action == 'transfer':
            from_account = input("Enter account number to transfer from: ").strip()
            to_account = input("Enter account number to transfer to: ").strip()
            amount = float(input("Enter amount to transfer (numbers only, no currency symbol): "))
            bank.transfer(from_account, to_account, amount)

        elif action == 'exit':
            print("Thank you for banking with us.")
            break

        else:
            print("Invalid action. Please choose a valid action.")

application()