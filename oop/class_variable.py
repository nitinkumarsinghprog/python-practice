class Employee:

    employee_count = 0

    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id
        Employee.employee_count += 1

    @classmethod
    def get_employee_count(cls):
        return cls.employee_count

emp1 = Employee("Rahul", 101)
emp2 = Employee("Amit", 102)
emp3 = Employee("Nitin", 103)

print(Employee.get_employee_count())