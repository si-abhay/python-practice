n=8
count=0
while(n!=0):
    if(n&1)==1:
        count+=1
    n>>=1
print(count)