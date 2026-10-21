# Abstract Class: Employee(ABC)
#   - __init__(name, emp_id, base_salary)
#       - self.name = name
#       - self.emp_id = emp_id
#       - self.__base_salary = base_salary    (private!)
#   - @abstractmethod calculate_salary() -> pass
#   - @abstractmethod get_role() -> pass
#   - get_base_salary() -> return self.__base_salary
#   - display() -> print name, emp_id, role, salary
#
# Child: Manager(Employee)
#   - __init__(name, emp_id, base_salary, bonus)
#   - calculate_salary() -> base_salary + bonus
#   - get_role() -> "Manager"
#
# Child: Developer(Employee)
#   - __init__(name, emp_id, base_salary, project_bonus)
#   - calculate_salary() -> base_salary + project_bonus
#   - get_role() -> "Developer"
#
# Child: Intern(Employee)
#   - __init__(name, emp_id, base_salary, stipend)
#   - calculate_salary() -> base_salary + stipend
#   - get_role() -> "Intern"

from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, emp_id, base_salary):
        self.name = name 
        self.emp_id = emp_id
        self.__base_salary = base_salary

    @abstractmethod
    def calculate_salary(self):
        pass

    @abstractmethod
    def get_role(self):
        pass

    def get_base_salary(self):
        return self.__base_salary

    def display(self):
        print(f"Name : {self.name}, Emp Id : {self.emp_id}, Role : {self.get_role()}, Salary : ₹{self.calculate_salary():,}")

class Manager(Employee):
    def __init__(self, name, emp_id, base_salary, bonus):
        super().__init__(name, emp_id, base_salary)
        self.bonus = bonus

    def calculate_salary(self):
        return self.bonus + self.get_base_salary()

    def get_role(self):
        return "Manager"

class Developer(Employee):
    def __init__(self, name, emp_id, base_salary, project_bonus):
        super().__init__(name, emp_id, base_salary)  
        self.project_bonus = project_bonus 

    def calculate_salary(self):
        return self.project_bonus + self.get_base_salary()
    
    def get_role(self):
        return "Developer"

class Intern(Employee):
    def __init__(self, name, emp_id, base_salary, stipend):
        super().__init__(name, emp_id, base_salary)
        self.stipend = stipend

    def calculate_salary(self):
        return self.stipend + self.get_base_salary()
        
    def get_role(self):
        return "Intern"


# ===== TEST CASES =====

print("=" * 50)
print("🧪 TEST 1: Abstract Class Instantiation (ERROR)")
print("=" * 50)

try:
    emp = Employee("Test", "E000", 10000)
except TypeError as e:
    print(f"❌ Error: {e}")


print("\n" + "=" * 50)
print("🧪 TEST 2: Manager Object")
print("=" * 50)

m = Manager("Amit Sharma", "E001", 60000, 10000)
m.display()
print(f"Calculated Salary: ₹{m.calculate_salary():,}")
print(f"Base Salary (getter): ₹{m.get_base_salary():,}")


print("\n" + "=" * 50)
print("🧪 TEST 3: Developer Object")
print("=" * 50)

d = Developer("Priya Singh", "E002", 50000, 15000)
d.display()
print(f"Calculated Salary: ₹{d.calculate_salary():,}")
print(f"Base Salary (getter): ₹{d.get_base_salary():,}")


print("\n" + "=" * 50)
print("🧪 TEST 4: Intern Object")
print("=" * 50)

i = Intern("Rahul Verma", "E003", 10000, 5000)
i.display()
print(f"Calculated Salary: ₹{i.calculate_salary():,}")
print(f"Base Salary (getter): ₹{i.get_base_salary():,}")


print("\n" + "=" * 50)
print("🧪 TEST 5: Private Attribute Access (ERROR)")
print("=" * 50)

try:
    print(m.__base_salary)
except AttributeError as e:
    print(f"❌ Error: {e}")

try:
    print(d.__base_salary)
except AttributeError as e:
    print(f"❌ Error: {e}")


print("\n" + "=" * 50)
print("🧪 TEST 6: Polymorphism - List of Employees")
print("=" * 50)

employees = [m, d, i]

for emp in employees:
    print(f"\n👤 {emp.name} ({emp.emp_id})")
    print(f"   Role   : {emp.get_role()}")
    print(f"   Salary : ₹{emp.calculate_salary():,}")


print("\n" + "=" * 50)
print("🧪 TEST 7: Total Payroll")
print("=" * 50)

total = sum(emp.calculate_salary() for emp in employees)
print(f"💰 Total Payroll: ₹{total:,}")