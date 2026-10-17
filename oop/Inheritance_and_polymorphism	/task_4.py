# Parent: Animal
#   - __init__(name)
#   - method: speak() -> "Some sound"
#   - method: info() -> "I am {name}"
#
# Children: Dog, Cat, Cow, Lion
# Har ek apna speak() override kare:
#   Dog  -> "Woof Woof"
#   Cat  -> "Meow Meow"
#   Cow  -> "Moo Moo"
#   Lion -> "Roar!"
#
# Ek list banao sab animals ki aur loop chalao speak() ke liye

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Animal making Sound"

    def info(self):
        print(f"I am {self.name}")

class Dog(Animal):
    def speak(self):
        return "Woof Woof"

class Cat(Animal):
    def speak(self):
        return "Meow Meow"

class Cow(Animal):
    def speak(self):
        return "Moo Moo"

class Lion(Animal):
    def speak(self):
        return "Roar !!!!"

animals = [
    Dog("Tommy"), Cat("Pussy"), Cow("Kamla"), Lion("Pram Dev")
]

for animal in animals:
    animal.info()          # "I am Tommy"
    print(f"{animal.name} says: {animal.speak()}")
    print("-" * 30)