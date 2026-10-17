
class Account:

    def __init__(self, account_no, holder_name, balance):
        self.account_no = account_no
        self.holder_name = holder_name
        self.balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance negative nahi ho sakta!")
        self._balance = value

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount positive hona chahiye!")

        self.balance += amount
        print(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw amount positive hona chahiye!")

        if amount > self.balance:
            print("Insufficient balance!")
            return

        self.balance -= amount
        print(f"Withdrawn: {amount}")

    def display_balance(self):
        print(f"Account No: {self.account_no}")
        print(f"Holder Name: {self.holder_name}")
        print(f"Balance: {self.balance}")


# Main
account = Account(101, "Nitin", 5000)

# Balance access (without parentheses)
print("Current Balance:", account.balance)

# Set positive balance
account.balance = 7000
print("Updated Balance:", account.balance)

# Set negative balance
try:
    account.balance = -1000
except ValueError as e:
    print("Error:", e)

# Deposit and withdraw
account.deposit(2000)
account.withdraw(1500)

# Display details
account.display_balance()
