class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        d = 2*k+1
        res = []
        if len(nums)<d:
            return [-1]*len(nums)
        for _ in range(min(len(nums),k)):
            res.append(-1)
        s = 0
        for i in range(d):
            s += nums[i]
        i = 0
        j = d
        res.append(s//d)
        while j<len(nums):
            s+=nums[j]
            s-=nums[i]
            j+=1
            i+=1
            res.append(s//d)
        while len(res)<len(nums):
            res.append(-1)
        return res