# Employee Management System

class Employee:
    def __init__(self, name, employee_id, salary, department):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
        self.department = department

    def display_details(self):
        print(f"Name : {self.name}")
        print(f"Employee Id : {self.employee_id}")
        print(f"Salary : {self.salary}")
        print(f"Department : {self.department}")

    def calculate_bonus(self):
        pass


class Developer(Employee):
    def __init__(self, name, employee_id, salary, department, programming_language):
        super().__init__(name, employee_id, salary, department)
        self.programming_language = programming_language

    def display_details(self):
        super().display_details()
        print(f"Developer : {self.programming_language}")

    def calculate_bonus(self):
        print(f"Bonus : {self.salary * 10 // 100}") 

class Designer(Employee):
    def __init__(self, name, employee_id, salary, department, design_tool):
        super().__init__(name, employee_id, salary, department)
        self.design_tool = design_tool

    def display_details(self):
        super().display_details()
        print(f"Design Tool : {self.design_tool}")

    def calculate_bonus(self):
            print(f"Bonus : {self.salary * 8 // 100}")
            

class Manager(Employee):
    def __init__(self, name, employee_id, salary, department, team_size):
        super().__init__(name, employee_id, salary, department)
        self.team_size = team_size

    def display_details(self):
        super().display_details()
        print(f"Team Size : {self.team_size}")

    def calculate_bonus(self):
            print(f"Bonus : {self.salary * 15 // 100}")


emp1 = Developer("Nitin", 101, 80000, "Engineering", "Python")
emp2 = Designer("Priya", 102, 70000, "Design", "Figma")
emp3 = Manager("Rahul", 103, 120000, "Engineering", 8)

employees = [emp1, emp2, emp3]

for employee in employees:
    employee.display_details()
    employee.calculate_bonus()


