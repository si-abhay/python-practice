
a=input().split()
n=int(a[0])
l=[int(i) for i in a[1:]]

#======= OR ========

a=input().split()
n=int(a[0])
l=[]
for i in a[1:]:
    l.append(int(i))

#input of form

#n 1 2 3 4


n=int(input())
l=[int(i) for i in input().split()]
#input of form

#n
#1 2 3 4


def fun():
    try:
        print("try block")
    except :
        print ("except block")
    else:
        print ("else block")
  
fun()


def fun(a):
    try :
        print(a/0)
    except :
        print ("except block")
    else:
        print ("else block")
  
fun(1)



def fun(a):
    try :
        print(a/0)
    except :
        print ("except block")
    else:
        print ("else block")
    finally:
        print("This is always run whether try block runs or except block")
  
fun(1)



pass




def fun(*params):
    for i in params:
        print(i)

l=[1,2,3,4]
fun(*l)



a=3
b=2
max=a if a>b else b
print("OUTPUT IS : ",max)