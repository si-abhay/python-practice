'''# Multiple Inheritance
class Student:
    def __init__(self,date):
        self.date=date
        print(f"Student 1st constructor {}")

    def __init__(self):
        print("Student 2nd constructor")
    def study(self):
        print("Studying")

s=Student(2)
'''


class Solution(object):     # 36/46 test case passsed
    def wordBreak(self, s, wordDict):
        for x in wordDict:
            ans=""
            m=s.split(x)
            for y in m:
                ans+=y
            s=ans
        if len(s)==0:
            return True
        else:
            return False