class BankAccount:

    def __init__(self, account_holder, account_number, balance):
        self.account_holder = account_holder
        self.account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            raise ValueError("Invalid amount ... ")
        
    def withdraw(self, amount):
        if amount > 0: 
            if amount <= self.__balance:
                self.__balance -= amount
            else:
                raise ValueError("Insufficient balance ... ")
        else:
            raise ValueError("Invalid withdrawal amount ... ")
        
    def get_balance(self):
        return self.__balance


account = BankAccount("Nitin", "ACC101", 10000)

account.deposit(5000)
account.withdraw(3000)

print(account.get_balance())