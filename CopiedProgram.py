#Copied Program from Programiz Joseph Rydberg 11/4/2024

class Student:
    def check_pass_fail(self):
        if self.marks >= 40:
            return True
        else:
            return False

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

student1 = Student("Harry", 85)
print(student1.name)
print(student1.marks)