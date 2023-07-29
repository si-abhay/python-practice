class Solution(object): 
    def queryString(self, s, n):
        for i in range(1, n+1):
            binary_rep = bin(i)[2:]
            if binary_rep not in s:
                return False
        return True