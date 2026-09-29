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


upi = UPIPayment()
upi.pay(1000)

credit = CreditCardPayment()
credit.pay(15000)

wallet = WalletPayment()
wallet.pay(4000)