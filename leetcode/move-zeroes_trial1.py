class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        res = []
        for i in nums:
            if i!=0:
                res.append(i)
        while len(res)<len(nums):
            res.append(0)
        for i in range(len(nums)):
            nums[i]=res[i]