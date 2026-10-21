# Class: Student
#   - __init__(name, marks)
#       - self.name = name                 (public)
#       - self._grade = "A"                (protected)
#       - self.__marks = marks             (private)
#
#   - method: set_marks(marks)
#       - agar marks < 0 or marks > 100: raise ValueError("Invalid marks")
#       - warna: self.__marks = marks
#       - Agar marks >= 90: self._grade = "A"
#       - Agar marks >= 75: self._grade = "B"
#       - Agar marks >= 60: self._grade = "C"
#       - Warna: self._grade = "D"
#
#   - method: get_marks() -> return self.__marks
#   - method: display() -> print name, marks, grade
#
# Main:
#   - Student object banao
#   - set_marks(95) -> grade "A"
#   - set_marks(80) -> grade "B"
#   - set_marks(150) -> ERROR
#   - display() call karo
#   - acc._grade access karo -> "A" (protected — ho sakta hai)
#   - acc.__marks access karo -> ERROR


class Student:
    def __init__(self, name, marks):
        self.name = name
        self._grade = "A"
        self.__marks = marks

    def set_marks(self, marks):
        if marks < 0 or marks > 100:
            raise ValueError("Invalid Marks ...")
        self.__marks = marks

        if marks >= 90:
            self._grade = "A"
        elif marks >= 75:
            self._grade = "B"
        elif marks >= 60:
            self._grade = "C"
        else:
            self._grade = "D"

    def get_marks(self):
        return self.__marks

    def display(self):
        print(f"Name : {self.name}, Marks : {self.__marks}, With Grade : {self._grade}")    

std1 = Student("Nitin", 76)

std1.set_marks(95)
std1.display()      # Marks: 95, Grade: A

std1.set_marks(80)
std1.display()      # Marks: 80, Grade: B

try:
    std1.set_marks(150)
except ValueError as e:
    print(f"❌ Error: {e}")

# Protected access
print(f"Protected grade: {std1._grade}")    # B

# Private access — ERROR
try:
    print(std1.__marks)
except AttributeError as e:
    print(f"❌ Error: {e}")

# Getter — sahi tarika
print(f"Marks via getter: {std1.get_marks()}")    # 80


        