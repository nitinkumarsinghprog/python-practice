class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary
    
    def work(self):
        print(f"{self.name} kaam kar raha hai")
    
    def show_details(self):
        print(f"ID: {self.emp_id}, Name: {self.name}, Salary: {self.salary}")

class Developer(Employee):
    def __init__(self, name, emp_id, salary, language):
        super().__init__(name, emp_id, salary)
        self.language = language
    
    def work(self):
        print(f"{self.name} {self.language} mein code likh raha hai")
    
    def show_details(self):
        super().show_details()
        print(f"Language: {self.language}")

class Manager(Employee):
    def __init__(self, name, emp_id, salary, team_size):
        super().__init__(name, emp_id, salary)
        self.team_size = team_size
    
    def work(self):
        print(f"{self.name} {self.team_size} logon ki team manage kar raha hai")

# Usage
dev = Developer("Amit", 101, 80000, "Python")
mgr = Manager("Priya", 102, 120000, 10)

dev.show_details()
dev.work()
print("-" * 50)
mgr.show_details()
mgr.work()