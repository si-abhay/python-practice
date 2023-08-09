class Pair :
    def __init__(self, minimum, maximum) :
        self.minimum = minimum
        self.maximum = maximum

from sys import maxsize
def getMinAndMax(root) :
    # base case
    if root is None:
        return Pair(maxsize,-maxsize)
    
    # hypothesis
    left=getMinAndMax(root.left)
    right=getMinAndMax(root.right)

    # small work
    min_m=min(root.data,min(left.minimum,right.minimum))
    max_m=max(root.data,max(left.maximum,right.maximum))
    
    return Pair(min_m,max_m)