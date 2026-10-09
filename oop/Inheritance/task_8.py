# Parent: Shape
#   - method: area() -> raise NotImplementedError
#   - method: perimeter() -> raise NotImplementedError
#   - method: describe() -> "I am a {class_name} with area {area}"
#
# Children: Circle, Rectangle, Square, Triangle
# Har shape ka area() aur perimeter() implement karo
#
# Ek list banao sab shapes ki
# Loop chalao aur total area print karo

class Shape:
    def area(self):
        raise NotImplementedError("Child must implement Area()")

    def perimeter(self):
        raise NotImplementedError("Child must implement Perimeter()")

    def describe(self):
        print(f"I am a {type(self).__name__} with area {self.area()}")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2
    
    def perimeter(self):
        return 4 * self.side

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def area(self):
        # Heron's formula
        s = (self.a + self.b + self.c) / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5
    
    def perimeter(self):
        return self.a + self.b + self.c

# ===== Main =====
shapes = [
    Circle(5),
    Rectangle(4, 6),
    Square(4),
    Triangle(3, 4, 5),
]

total_area = 0

for shape in shapes:
    shape.describe()                         
    print(f"Perimeter: {shape.perimeter()}") 
    total_area += shape.area()                

print(f"\nTotal Area: {total_area}")