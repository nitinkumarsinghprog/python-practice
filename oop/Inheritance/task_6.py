# Parent: Employee
#   - name, emp_id, base_salary
#   - calculate_salary() -> base_salary
#   - display()
#
# Child: FullTimeEmployee
#   - extra: bonus
#   - calculate_salary() -> base + bonus
#
# Child: PartTimeEmployee
#   - extra: hours_worked, hourly_rate
#   - calculate_salary() -> hours * rate
#
# Child: Contractor
#   - extra: contract_amount
#   - calculate_salary() -> contract_amount
#
# Sab employees ki list banao, total payroll calculate karo

# ===== All Classes (same as yours) =====
class Employee:
    def __init__(self, name, emp_id, base_salary):
        self.name = name
        self.emp_id = emp_id
        self.base_salary = base_salary

    def calculate_salary(self):
        return self.base_salary

    def display(self):
        print(f"Name        : {self.name}")
        print(f"Employee ID : {self.emp_id}")
        print(f"Type        : {type(self).__name__}")

    def __str__(self):
        return f"{self.name} ({self.emp_id})"


class FullTimeEmployee(Employee):
    def __init__(self, name, emp_id, base_salary, bonus):
        super().__init__(name, emp_id, base_salary)
        self.bonus = bonus

    def calculate_salary(self):
        return self.base_salary + self.bonus


class PartTimeEmployee(Employee):
    def __init__(self, name, emp_id, base_salary, hours_worked, hourly_rate):
        super().__init__(name, emp_id, base_salary)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return self.hours_worked * self.hourly_rate


class Contractor(Employee):
    def __init__(self, name, emp_id, base_salary, contract_amount):
        super().__init__(name, emp_id, base_salary)
        self.contract_amount = contract_amount

    def calculate_salary(self):
        return self.contract_amount


# ===== MAIN PROGRAM =====
employees = [
    FullTimeEmployee("Amit Sharma", "E001", 60000, 10000),
    PartTimeEmployee("Priya Singh", "E002", 0, 80, 500),
    Contractor("Rahul Verma", "E003", 0, 75000),
    FullTimeEmployee("Sneha Patel", "E004", 60000, 15000),
    PartTimeEmployee("Karan Mehta", "E005", 0, 100, 600),
    Contractor("Anita Desai", "E006", 0, 90000),
]

print("=" * 30)
print("💼 EMPLOYEE PAYROLL SYSTEM")
print("=" * 30)

for emp in employees:
    print(f"\n👤 {emp}")
    emp.display()
    print(f"💰 Salary: ₹{emp.calculate_salary():,}")
    print("-" * 30)

# Statistics
total = sum(emp.calculate_salary() for emp in employees)
average = total // len(employees)
highest = max(employees, key=lambda e: e.calculate_salary())

print(f"\n{'=' * 30}")
print(f"📊 PAYROLL SUMMARY")
print(f"{'=' * 30}")
print(f"👥 Total Employees : {len(employees)}")
print(f"💰 Total Payroll   : ₹{total:,}")
print(f"📈 Average Salary  : ₹{average:,}")
print(f"🏆 Highest Paid    : {highest} - ₹{highest.calculate_salary():,}")
print(f"{'=' * 30}")