
from abc import ABC, abstractmethod
import math


# Parent Abstract Class
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def describe(self):
        return f"I am a {self.__class__.__name__} with area {self.area():.2f}"


# Child Class: Circle
class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


# Child Class: Rectangle
class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


# Child Class: Square
class Square(Shape):

    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side


# Child Class: Triangle
class Triangle(Shape):

    def __init__(self, a, b, c):
        if (a + b <= c or a + c <= b or b + c <= a):
            raise ValueError("Invalid triangle sides")

        self.a = a
        self.b = b
        self.c = c

    def area(self):
        # Heron's formula
        s = self.perimeter() / 2
        return math.sqrt(
            s * (s - self.a) * (s - self.b) * (s - self.c)
        )

    def perimeter(self):
        return self.a + self.b + self.c


# Main
try:
    shape = Shape()
except TypeError as e:
    print("Error:", e)


shapes = [
    Circle(5),
    Rectangle(10, 5),
    Square(4),
    Triangle(3, 4, 5)
]

total_area = 0

for shape in shapes:
    print(shape.describe())
    print(f"Perimeter: {shape.perimeter():.2f}")
    total_area += shape.area()

print(f"Total area: {total_area:.2f}")
