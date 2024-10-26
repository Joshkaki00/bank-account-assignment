class BankAccount:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance
        pass

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

