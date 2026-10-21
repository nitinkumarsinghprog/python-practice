# Abstract Class: PaymentMethod(ABC)
#   - @abstractmethod process_payment(amount) -> pass
#   - @abstractmethod refund(amount) -> pass
#
# Child: CreditCard(PaymentMethod)
#   - __init__(card_number, cvv)
#   - process_payment(amount) -> print "Processing ₹{amount} via CreditCard ending {last4}"
#   - refund(amount) -> print "Refund ₹{amount} to CreditCard"
#
# Child: UPI(PaymentMethod)
#   - __init__(upi_id)
#   - process_payment(amount) -> print "Processing ₹{amount} via UPI: {upi_id}"
#   - refund(amount) -> print "Refund ₹{amount} to UPI"
#
# Child: Wallet(PaymentMethod)
#   - __init__(wallet_id, balance)
#       - self.__balance = balance    (private!)
#   - process_payment(amount)
#       - agar amount > self.__balance: print "Insufficient balance!"
#       - warna: self.__balance -= amount + print "Paid ₹{amount} via Wallet {wallet_id}"
#       - print "Remaining Balance: ₹{self.__balance}"
#   - refund(amount)
#       - self.__balance += amount
#       - print "Refunded ₹{amount} to Wallet {wallet_id}"
#       - print "New Balance: ₹{self.__balance}"
#   - get_balance() -> return self.__balance
#
# Main:
#   - PaymentMethod() object banane ki koshish karo -> ERROR
#   - 3 objects banao (CreditCard, UPI, Wallet)
#   - Sabka process_payment() call karo
#   - Sabka refund() call karo
#   - Wallet ka __balance access karo -> ERROR
#   - Wallet ka get_balance() call karo

from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

    @abstractmethod
    def refund(self, amount):
        pass

class CreditCard(PaymentMethod):
    def __init__(self, card_number, cvv):
        super().__init__()
        self.card_number = card_number
        self.cvv = cvv

    def process_payment(self, amount):
        print(f"Processing ₹{amount} via CreditCard ending {self.card_number[-4:]}")

    def refund(self, amount):
        print(f"Refund ₹{amount} to CreditCard")

class UPI(PaymentMethod):
    def __init__(self, upi_id):
        super().__init__()
        self.upi_id = upi_id

    def process_payment(self, amount):
        print(f"Processing ₹{amount} via UPI: {self.upi_id}")
    
    def refund(self, amount):
        print(f"Refund ₹{amount} to UPI")

class Wallet(PaymentMethod):
    def __init__(self, wallet_id, balance):
        super().__init__()
        self.wallet_id = wallet_id
        self.__balance = balance

    def process_payment(self, amount):
        if amount > self.__balance:
            print("Insufficient balance!")
        else: 
            self.__balance -= amount
            print(f"Paid ₹{amount} via Wallet {self.wallet_id}")
            print(f"Remaining Balance: ₹{self.__balance}")

    def refund(self, amount):
        self.__balance += amount
        print(f"Refunded ₹{amount} to Wallet {self.wallet_id}")
        print(f"New Balance: ₹{self.__balance}")

    def get_balance(self):
        return self.__balance

# ===== TEST CASES =====

# 1. Abstract class ka object — ERROR
try:
    pm = PaymentMethod()
except TypeError as e:
    print(f"❌ Error: {e}")

print()

# 2. CreditCard test
cc = CreditCard("1234567890123456", "123")
cc.process_payment(500)
cc.refund(500)

print()

# 3. UPI test
upi = UPI("user@upi")
upi.process_payment(1000)
upi.refund(1000)

print()

# 4. Wallet test
w = Wallet("W001", 2000)
w.process_payment(500)
w.refund(500)

print()

# 5. Wallet private balance access — ERROR
try:
    print(w.__balance)
except AttributeError as e:
    print(f"❌ Error: {e}")

# 6. Wallet getter — sahi tarika
print(f"Balance via getter: ₹{w.get_balance()}")