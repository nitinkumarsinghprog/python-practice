# Polymorphism

class Payment:
    def pay(self, amount):
        pass


class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Payment of {amount} using Credit Card")


class UPIPayment(Payment):
    def pay(self, amount):
        print(f"Payment of {amount} using UPI")


class PayPalPayment(Payment):
    def pay(self, amount):
        print(f"Payment of {amount} using PayPal")


payments = [
    CreditCardPayment(),
    UPIPayment(),
    PayPalPayment()
]

for payment in payments:
    payment.pay(5000)