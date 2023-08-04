class Student:
    def __init__(self):
        print("Student 2nd constructor -----  when data not given")
    
    def __init__(self,data):
        self.data=data
        print(f"Student 1st constructor ----   {self.data}")
        print("It works as")
        print("the last same name function is what exists")
        print("others consider them as overwritten by last")

    def study(self):
        print("Studying")

s=Student(3)
s=Student()