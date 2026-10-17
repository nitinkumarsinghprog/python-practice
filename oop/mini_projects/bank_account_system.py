from datetime import datetime


# ===================== PARENT CLASS =====================
class Account:
    def __init__(self, account_no, holder_name, balance):
        self.account_no = account_no
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"✅ Deposited: ₹{amount:,}")
        print(f"   New Balance: ₹{self.balance:,}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"✅ Withdrawn: ₹{amount:,}")
            print(f"   New Balance: ₹{self.balance:,}")
        else:
            print(f"❌ Insufficient Balance! Available: ₹{self.balance:,}")

    def display_balance(self):
        print(f"Account No : {self.account_no}")
        print(f"Holder     : {self.holder_name}")
        print(f"Balance    : ₹{self.balance:,}")


# ===================== SAVINGS ACCOUNT =====================
class SavingsAccount(Account):
    def __init__(self, account_no, holder_name, balance, interest_rate):
        super().__init__(account_no, holder_name, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        print(f"✅ Interest Added: ₹{interest:,} ({self.interest_rate}%)")
        print(f"   New Balance: ₹{self.balance:,}")

    def withdraw(self, amount):
        if amount > 50000:
            print(f"❌ Daily limit exceeded! Max: ₹50,000")
            return
        super().withdraw(amount)   # Parent ka withdraw call karo


# ===================== CURRENT ACCOUNT =====================
class CurrentAccount(Account):
    def __init__(self, account_no, holder_name, balance, overdraft_limit):
        super().__init__(account_no, holder_name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"✅ Withdrawn: ₹{amount:,}")
            if self.balance < 0:
                print(f"⚠️  Warning: Overdraft used!")
            print(f"   New Balance: ₹{self.balance:,}")
        else:
            print(f"❌ Exceeds overdraft limit! Max withdraw: ₹{self.balance + self.overdraft_limit:,}")


# ===================== FIXED DEPOSIT =====================
class FixedDeposit(Account):
    def __init__(self, account_no, holder_name, balance, tenure, maturity_date):
        super().__init__(account_no, holder_name, balance)
        self.tenure = tenure
        self.maturity_date = datetime.strptime(maturity_date, "%Y-%m-%d").date()

    def withdraw(self, amount):
        today = datetime.now().date()
        if today < self.maturity_date:
            print(f"❌ Cannot withdraw before maturity! Matures on {self.maturity_date}")
        else:
            super().withdraw(amount)

    def display_balance(self):
        super().display_balance()
        print(f"Tenure     : {self.tenure}")
        print(f"Maturity   : {self.maturity_date}")


# ===================== MAIN =====================
print("=" * 50)
print("🏦 BANK ACCOUNT SYSTEM")
print("=" * 50)

# --- Savings Account ---
print("\n--- Savings Account ---")
sav = SavingsAccount("S001", "Amit Sharma", 50000, 5)
sav.display_balance()
print()
sav.deposit(10000)
print()
sav.add_interest()
print()
sav.withdraw(55000)    # ❌ Limit exceeded
print()
sav.withdraw(40000)    # ✅
print("-" * 50)

# --- Current Account ---
print("\n--- Current Account ---")
cur = CurrentAccount("C001", "Priya Singh", 10000, 5000)
cur.display_balance()
print()
cur.withdraw(14000)    # ✅ Overdraft used
print()
cur.withdraw(5000)     # ❌ Exceeds overdraft
print("-" * 50)

# --- Fixed Deposit ---
print("\n--- Fixed Deposit ---")
fd = FixedDeposit("F001", "Rahul Verma", 100000, "2 years", "2026-12-31")
fd.display_balance()
print()
fd.withdraw(50000)     # ❌ Not mature yet
print("-" * 50)

# --- List + Loop (Polymorphism) ---
print("\n--- All Accounts Summary ---")
accounts = [sav, cur, fd]
for acc in accounts:
    print(f"\n👤 {acc.holder_name} ({acc.account_no})")
    print(f"   Balance: ₹{acc.balance:,}")