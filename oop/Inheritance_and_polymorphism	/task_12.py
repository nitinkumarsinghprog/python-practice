# LivingThing
#   - method: breathe() -> "Breathing..."
#   - method: eat() -> "Eating..."
#
# Animal(LivingThing)
#   - method: move() -> "Moving..."
#   - method: sleep() -> "Sleeping..."
#
# Mammal(Animal)
#   - method: give_birth() -> "Giving birth..."
#   - method: feed_milk() -> "Feeding milk..."
#
# Human(Mammal)
#   - method: think() -> "Thinking..."
#   - method: speak() -> "Speaking..."
#   - method: code() -> "Coding... 👨‍💻"
#
# Test karo: Human object banao, sab 9 methods call karo

class LivingThing:
    def breathing(self):
        return "Breathing..."
    def eat(self):
        return "Eating..."

class Animal(LivingThing):
    def move(self):
        return "Moving..."
    def sleep(self):
        return "Sleeping..."

class Mammal(Animal):
    def give_birth(self):
        return "Giving birth..."
    def feed_milk(self):
        return "Feeding milk..."

class Human(Mammal):
    def think(self):
        return "Thinking..."
    def speak(self):
        return "Speaking..."
    def code(self):
        return "Coding... 👨‍💻"

hm = Human()

print(hm.breathing())
print(hm.eat())
print(hm.move())
print(hm.sleep())
print(hm.give_birth())
print(hm.feed_milk())
print(hm.think())
print(hm.speak())
print(hm.code())
print(Human.__mro__)


    