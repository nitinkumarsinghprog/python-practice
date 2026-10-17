#Inheritance matlab Ek class doosri class ke features use kar sakti hai bina dobara likhe.

class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):   # Dog ne Animal ko inherit kiya
    def bark(self):
        print(f"{self.name} says: Woof!")

d = Dog("Tommy")
d.eat()      # Parent se aaya
d.sleep()    # Parent se aaya
d.bark()     # Apna method