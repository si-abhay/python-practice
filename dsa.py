class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def takeinput():
    rootdata=int(input())
    if rootdata==-1:
        return None
    else:
        root=node(rootdata)
        root.left=takeinput()
        root.right=takeinput()
    
    return root

def printit(root):
    if root:
        print(root.data,end=": ")
        if root.left:
            print("L",root.left.data,end=", ")
        if root.right:
            print("R",root.right.data,end="")
        print()
        printit(root.left)
        printit(root.right)
    else:
        return


root=takeinput()
printit(root)
