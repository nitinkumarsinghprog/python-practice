# Class: BankAccount
#   - __init__(account_no, holder_name, balance)
#   - __str__() -> "A001 - Amit (₹5000)"
#   - __eq__(other) -> True agar account_no same ho
#   - __add__(other) -> naya BankAccount with:
#       account_no = "COMBINED"
#       holder_name = "Combined Account"
#       balance = self.balance + other.balance
#   - __lt__(other) -> True agar self.balance < other.balance
#
# Main:
#   - 3 accounts banao
#   - __str__ test karo -> print(acc)
#   - __eq__ test karo -> acc1 == acc2
#   - __add__ test karo -> acc1 + acc2
#   - __lt__ test karo -> acc1 < acc2



class BankAccount:

    def __init__(self, account_no, holder_name, balance):
        self.account_no = account_no
        self.holder_name = holder_name
        self.balance = balance

    def __str__(self):
        return f"{self.account_no} - {self.holder_name} (₹{self.balance})"

    def __eq__(self, other):
        if not isinstance(other, BankAccount):
            return NotImplemented

        return self.account_no == other.account_no

    def __add__(self, other):
        if not isinstance(other, BankAccount):
            return NotImplemented

        return BankAccount(
            "COMBINED",
            "Combined Account",
            self.balance + other.balance
        )

    def __lt__(self, other):
        if not isinstance(other, BankAccount):
            return NotImplemented

        return self.balance < other.balance


# Test cases
a1 = BankAccount("A001", "Amit", 5000)
a2 = BankAccount("A002", "Priya", 3000)
a3 = BankAccount("A001", "Amit", 9999)

print(a1)              # A001 - Amit (₹5000)
print(a1 == a2)        # False
print(a1 == a3)        # True (same account_no)
print(a1 < a2)         # False
print(a2 < a1)         # True

combined = a1 + a2
print(combined)        # COMBINED - Combined Account (₹8000)
