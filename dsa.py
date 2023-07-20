from array import array
l=array('I',[])

n=int(input())

for i in range(n):
    x=int(input(f'Enter the {i}th element'))
    l.append(x)

print(l)