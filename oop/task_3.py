# Inheritance + super()

class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_details(self):
        print(f"Name : {self.name}")
        print(f"Employee Id : {self.employee_id}")
        print(f"Salary : {self.salary}")

class Developer(Employee):
    def __init__(self, name, employee_id, salary, programming_language):
        super().__init__(name, employee_id, salary)
        self.programming_language = programming_language

    def display_details(self):
        super().display_details()
        print(f"Programming Language : {self.programming_language}")

class Manager(Employee):
    def __init__(self, name, employee_id, salary, team_size):
        super().__init__(name, employee_id, salary)
        self.team_size = team_size

    def display_details(self):
        super().display_details()
        print(f"Team Size : {self.team_size}")


developer = Developer(
    "Nitin",
    101,
    80000,
    "Python"
)

manager = Manager(
    "Rahul",
    102,
    120000,
    8
)

developer.display_details()
manager.display_details()