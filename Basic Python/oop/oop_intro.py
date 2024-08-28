class Student:

    def __init__(self, name, grades):
        # print(self)
        self.name = name
        self.grades = grades

    def average_grades(self):
        print(self)
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        return f"Hi, this is {self.name}"

    def __repr__(self):
        return f"Student: {self.name} & {self.grades}"


student1 = {
    "name": "Naren",
    "grades": (4, 5, 2, 5, 2)
}

student2 = {
    "name": "Naren2",
    "grades": (8, 6, 4, 3, 3)
}

student_obj1 = Student(student1["name"], student1["grades"])
student_obj2 = Student(student2["name"], student2["grades"])

print(student_obj1)
print(student_obj1.__repr__())
print(student_obj1.average_grades())

print(student_obj2)
print(student_obj2.__repr__())
print(student_obj2.average_grades())
