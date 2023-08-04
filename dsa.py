# Multiple Inheritance
class Student:
    def __init__(self,date):
        self.date=date
        print("Student constructor")
    def study(self):
        print("Studying")

class Teacher:
    def __init__(self,name):
        self.name=name
        print("Teacher constructor")
    def teach(self):
        print("Teacher")

class TA (Student, Teacher):
    def work(self):
        print("Working")

t = TA()