class Solution:
    def topKFrequent(self, nums, k):
        maps={}
        for n in nums:
            maps[n]= 1 + maps.get(n,0)

        freq = [[] for i in range(len(nums)+1)]
        for n,count in maps.items():
            freq[count].append(n)
