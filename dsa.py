
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