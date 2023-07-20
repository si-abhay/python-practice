l=[[1,2,3],[4,5,6],[7,8,9]]

ans=[[] for i in range(len(l))]  #2D Array empty initialization

for i in range(len(l)):
    for j in range(len(l[0])):
        sum=0                    # Look where sum is initialized
        for x in l[i][j+1:]:     # j+1 is out of bound for last element still it works and thus does nothing to sum and 0 is appended
            sum+=x
        ans[i].append(sum)

print(ans)

#=================OPTIMISED n*n approach=========>

l=[[1,2,3],[4,5,6],[7,8,9]]

n = len(l)
m = len(l[0])
# Loop to create the new sum which is sum of elements to the right
for i in range(n):
    sum = 0
    for j in range(m-1 , -1, -1):
        temp = l[i][j]
        # Storing array value in a temp variable
        l[i][j] = sum
        sum += temp
# Returning the new matrix after performing summation return arr
print(l)