from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class UPIPayment(Payment):
    def pay(self, amount):
        print(f"Payment of {amount} done using UPI")
class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Payment of {amount} done using Credit Card")
class WalletPayment(Payment):
    def pay(self, amount):
        print(f"Payment of {amount} done using Wallet")
class PaymentFactory:
    @staticmethod
    def create_payment(payment_type):
        if payment_type == "upi":
            return UPIPayment()
        elif payment_type == "card":
            return CreditCardPayment()
        elif payment_type == "wallet":
            return WalletPayment()
        else:
            raise ValueError("Invalid Method")

payment = PaymentFactory.create_payment("upi")
payment.pay(1000)

payment = PaymentFactory.create_payment("card")
payment.pay(15000)

payment = PaymentFactory.create_payment("wallet")
payment.pay(4000)