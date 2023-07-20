# Bubble sort

# after each iteration one largest element will go to it's final position
# for eg in l=[10,5,9,4,2]
# after first iteration 10 will be at it's original pos output of first iteration : [5,9,4,2,10]
# second iteration [5,4,2,9,10]
# third iteration [4,2,5,9,10]

l=[10,5,9,4,2]
n=len(l)
for i in range(n-1):
    for j in range(n-1):
        if l[j]>l[j+1]:
            temp=l[j]
            l[j]=l[j+1]
            l[j+1]=temp
print(l)