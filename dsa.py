class newNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder(temp): 
    if (not temp):
        return
    inorder(temp.left)
    print(temp.data, end=" ")
    inorder(temp.right)

def insert(temp,key):
    if temp is None:
        return newNode(key)
    q=[]
    q.append(temp)
    while(q):
        x=q.pop(0)
        if x.left:
            q.append(x.left)
        else:
            x.left=newNode(key)
            break
        if x.right:
            q.append(x.right)
        else:
            x.right=newNode(key)
            break
    return temp


def findel(temp,key):
    global count
    if temp is None:
        return
    if temp.data==key:
        print(count)
        return True
    if temp.left:
        findel(temp.left,key)
    if temp.right:
        findel(temp.right,key)
    return False
    

#Driver code
if __name__ == '__main__':
    root = newNode (10) 
    root.left = newNode (11)
    root.left.left = newNode(7) 
    root.right= newNode(9)
    root.right.left = newNode(15) 
    root.right.right = newNode (8)
    inorder (root)
    insert(root, 12)
    print()
    inorder (root)
    print(findel(root,7))