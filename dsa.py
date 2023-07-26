def create():
    stack=[]
    return stack

def is_empty(stack):
    return len(stack)==0

def push(stack,element):
    stack.append(element)
    return stack

def pop_ele(stack):
    if is_empty(stack):
        return -1
    else:
        return stack.pop()
    
stack=create()

push(stack,1)
push(stack,2)
push(stack,3)
push(stack,4)

print(stack)
print(pop_ele(stack))