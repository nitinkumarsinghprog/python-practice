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

class Order:
    def __init__(self, payment):
        self.payment = payment

    def checkout(self, amount):
        return self.payment.pay(amount)


payment = PaymentFactory.create_payment("upi")
order = Order(payment)
order.checkout(1000)

payment = PaymentFactory.create_payment("card")
order = Order(payment)
order.checkout(15000)

payment = PaymentFactory.create_payment("wallet")
order = Order(payment)
order.checkout(4000)