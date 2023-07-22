l=[1,3,2,2,4]
map=[False for i in l]

def finddup(l):
    for i in l:
        if map[i-1]:
            return i
        else:
            map[i-1]=True

