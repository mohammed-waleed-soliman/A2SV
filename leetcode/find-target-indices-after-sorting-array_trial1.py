class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            for j in range(len(nums)-1):
                if(nums[j]>nums[j+1]):
                    temp = nums[j]
                    nums[j] = nums[j+1]
                    nums[j+1] = temp
        res = []
        for i in range(len(nums)):
            if nums[i]==target:
                res.append(i)
        return res