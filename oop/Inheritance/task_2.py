# using Super method 

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, roll_no):
        super().__init__(name, age)   # Parent ka constructor call kiya
        self.roll_no = roll_no
    
    def display(self):
        super().display()              # Parent ka method call kiya
        print(f"Roll No: {self.roll_no}")

s = Student("Rahul", 20, 101)
s.display()