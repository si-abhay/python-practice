'''
class Solution(object):     #22/28 test case passed
    def queryString(self, s, n):
        q=[]
        q.append("1")
        for i in range(1,n):
            temp=q.pop(0)
            if (temp+"0" in s) and (temp+"1" in s):
                q.append(temp+"0")
                q.append(temp+"1")
            else:
                return False  
        return True
'''


s="1011"
i=int(s)
print(i)