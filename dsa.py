l=[-5, 4, 6, -3, 4, 1]
max_sum=-float('inf')
n=len(l)
sum=0
ans=[]
ls=[]
for i in range(n):
    sum+=l[i]
    ls.append(l[i])
    if sum<0 and i !=0:
        sum=0
        ls.clear()
    if max_sum<sum:
        max_sum=sum
        ans=ls[0:]

print(max_sum)
print(ans)