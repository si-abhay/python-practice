# class and objects sizes
# ==== TO DO ========

class School:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.teachers = []
        
    def add_student(self, student):
        self.students.append(student)
        
    def add_teacher(self, teacher):
        self.teachers.append(teacher)
        
    def show_info(self):
        print(f"School: {self.name}")
        print("Students:")
        for student in self.students:
            student.show()
        print("Teachers:")
        for teacher in self.teachers:
            teacher.show()
        
    class Student:
        def __init__(self, name, grade):
            self.name = name
            self.grade = grade
            
        def show(self):
            print(f"Student: {self.name}, Grade: {self.grade}")
            
    class Teacher:
        def __init__(self, name, subject):
            self.name = name
            self.subject = subject
            
        def show(self):
            print(f"Teacher: {self.name}, Subject: {self.subject}")


school = School("ABC School")


stu1 = school.Student("Alice", 9)
stu2 = school.Student("Bob", 10)

teach1 = school.Teacher("Ms. Smith", "Math")
teach2 = school.Teacher("Mr. Johnson", "Science")


school.add_student(stu1)
school.add_student(stu2)

school.add_teacher(teach1)
school.add_teacher(teach2)

school.show_info()
