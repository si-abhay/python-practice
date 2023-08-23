class Solution:
    def productExceptSelf(self, nums):
        ans=[]
        start=1
        after=1
        for i in range(len(nums)):
            ans.append(start)
            start*=nums[i]
        for i in range(len(nums)-1,-1,-1):
            ans[i]*=after
            after*=nums[i]
        return ans