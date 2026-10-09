# Parent: PaymentMethod
#   - method: process_payment(amount) -> raise NotImplementedError
#   - method: refund(amount) -> raise NotImplementedError
#
# Children:
#   - CreditCard(card_number, cvv)
#   - UPI(upi_id)
#   - NetBanking(bank_name, account_no)
#   - Wallet(wallet_id, balance)
#
# Har ek apna process_payment implement kare
# Wallet mein balance check karo pehle

class PaymentMethod:
    def process_payment(self, amount):
        raise NotImplementedError("Child must Implement Proccess Payment")

    def refund(self, amount):
        raise NotImplementedError("Chile must Implemnt Refund ")

class CreditCard(PaymentMethod):
    def __init__(self, card_number, cvv):
        self.card_number = card_number
        self.cvv = cvv

    def process_payment(self, amount):
        print(f"Processing ₹{amount} via CreditCard ending {self.card_number}") 

    def refund(self, amount):
        print(f"Refund ₹{amount} to CreditCard") 

class UPI(PaymentMethod):
    def __init__(self, upi_id):
        self.upi_id = upi_id

    def process_payment(self, amount):
        print(f"Processing ₹{amount} via UPI : {self.upi_id}") 
    
    def refund(self, amount):
        print(f"Refund ₹{amount} to UPI") 

class NetBanking(PaymentMethod):
    def __init__(self, bank_name, account_no):
        self.bank_name = bank_name
        self.account_no = account_no

    def process_payment(self, amount):
        print(f"Processing ₹{amount} via Net Banking from Account : {self.account_no}") 

    def refund(self, amount):
        print(f"Refund ₹{amount} to account {self.account_no}") 

class Wallet(PaymentMethod):
    def __init__(self, wallet_id, balance):
        self.wallet_id = wallet_id
        self.balance = balance

    def process_payment(self, amount):
        if amount > self.balance:
            print(f"❌ Insufficient balance! Available: ₹{self.balance}")
        else:
            self.balance -= amount
            print(f"✅ ₹{amount} paid via Wallet {self.wallet_id}")
            print(f"   Remaining Balance: ₹{self.balance}") 

    def refund(self, amount):
        self.balance += amount
        print(f"✅ ₹{amount} refunded to Wallet {self.wallet_id}")
        print(f"   New Balance: ₹{self.balance}")

payments = [
    CreditCard("1234567890123456", "123"),
    UPI("user@upi"),
    NetBanking("HDFC", "9876543210"),
    Wallet("W001", 2000),
]

for p in payments:
    p.process_payment(500)    
    p.refund(200)             