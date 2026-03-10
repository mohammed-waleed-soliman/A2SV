class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        mx = 0
        i = 0
        j = k
        for m in range(k):
            mx+=nums[m]
        res = mx
        while j<len(nums):
            mx-=nums[i]
            mx+=nums[j]
            i+=1
            j+=1
            res = max(res,mx)
        return res/k