class BankAccount:
    def __init__(self, account_holder, account_number, balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("Invalid Amount")
        
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
        else:
            raise ValueError("Insufficient balance")
        
    def check_balance(self):
        print(self.balance)

account = BankAccount("Nitin", "ACC101", 5000)

account.deposit(2000)
account.withdraw(1500)

account.check_balance()

