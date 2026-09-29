
class Employee:
    def __init__(self, name, employee_id, department, salary):
        self.name = name
        self.employee_id = employee_id
        self.department = department
        self.salary = salary

    def display_details(self):
        print(f"Name : {self.name}")
        print(f"Employee ID : {self.employee_id}")
        print(f"Department : {self.department}")
        print(f"Salary : {self.salary}")

    def give_raise(self, amount):
        if amount > 0:
            self.salary += amount
        else:
            raise ValueError("Invalid Amount ... ")

    def is_high_earner(self):
        if self.salary >= 100000:
            return True
        else:
            return False

emp1 = Employee("Rahul", 101, "Engineering", 85000)
emp2 = Employee("Amit", 102, "HR", 120000)


emp1.display_details()
emp2.display_details()

emp1.give_raise(20000)
emp2.give_raise(-5000)


print(emp1.is_high_earner())
print(emp2.is_high_earner())