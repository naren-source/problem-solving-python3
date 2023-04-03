from typing import List, Optional


class Student:
    def __init__(self, name: str, grades: List[int] = None):
        self.name = name
        self.grades = grades or []

    def take_exam(self, result: int):
        self.grades.append(result)


a = Student("a")
b = Student("b")
a.take_exam(90)
print(a.grades)
print(b.grades)
