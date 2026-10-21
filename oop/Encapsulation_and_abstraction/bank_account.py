# Class: BankAccount
#   - __init__(holder_name, balance)
#       - self.__balance = balance       (private)
#       - self._account_no = "A001"      (protected)
#       - self.holder_name = holder_name (public)
#
#   - method: deposit(amount)
#       - agar amount <= 0: raise ValueError("Invalid amount")
#       - warna: self.__balance += amount
#
#   - method: withdraw(amount)
#       - agar amount <= 0: raise ValueError("Invalid amount")
#       - agar amount > self.__balance: print("Insufficient balance")
#       - warna: self.__balance -= amount
#
#   - method: get_balance() -> return self.__balance
#
# Main:
#   - BankAccount object banao
#   - deposit(), withdraw() test karo
#   - acc.__balance access karne ki koshish karo -> ERROR
#   - acc._BankAccount__balance se access karo -> 1000 (name mangling demo)
#   - acc.get_balance() se sahi tarika dikhao


class BankAccount:
    def __init__(self, holder_name, account_no, balance):
        self.holder_name = holder_name
        self._account_no = account_no
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Invalid amount")
        else:
            self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Invalid Amount...")
        elif amount > self.__balance:
            print("Insufficient Balance")
        else:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

acc = BankAccount("Nitin", "AA0821", 10000)

# ===== TEST CASES =====

# 1. Public access — sahi
print(acc.holder_name)        # Nitin ✅

# 2. Protected access — ho sakta hai, but shouldn't
print(acc._account_no)        # AA0821 ⚠️

# 3. Private access — ERROR aayega
try:
    print(acc.__balance)
except AttributeError as e:
    print(f"❌ Error: {e}")

# 4. Private access via getter — SAHI TARIKA
print(f"Balance: ₹{acc.get_balance():,}")    # ₹10,000 ✅

# 5. Name mangling — private access ka "hack"
print(f"Name mangling: {acc._BankAccount__balance}")    # 10000

# 6. Deposit test
acc.deposit(5000)
print(f"After deposit: ₹{acc.get_balance():,}")    # ₹15,000

# 7. Deposit invalid
try:
    acc.deposit(-100)
except ValueError as e:
    print(f"❌ Error: {e}")

# 8. Withdraw test
acc.withdraw(3000)
print(f"After withdraw: ₹{acc.get_balance():,}")    # ₹12,000

# 9. Withdraw insufficient
acc.withdraw(50000)
# "Insufficient Balance"

# 10. Withdraw invalid
try:
    acc.withdraw(-100)
except ValueError as e:
    print(f"❌ Error: {e}")


