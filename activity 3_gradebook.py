class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score


# Gradebook class
class Gradebook:
    def __init__(self):
        self.students = []  
    def add_student(self, student):
        self.students.append(student)

    def get_average(self):
        total = 0
        for student in self.students:
            total += student.score

        if len(self.students) == 0:
            return 0

        return total / len(self.students)


# Testing the program
s1 = Student("Janeth", 85)
s2 = Student("Imelda", 90)
s3 = Student("Careen", 78)

gradebook = Gradebook()
gradebook.add_student