# //20,3,1,19,21,4,2
# (1,2,3,4)(19,20,21)
global maxi
def _lis(arr,n):
    
    if n==1:
        return 1
    maxEndhere=1
    for i in range(1,n):
        res=_lis(arr,i)
        if arr[i-1]<arr[n-1] and res+1>maxEndhere:
            maxEndhere=res+1
    maxi=max(maxi,maxEndhere)
    return maxEndhere


