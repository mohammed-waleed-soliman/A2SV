class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        ind = len(nums)-k
        res=[]
        for i in range(ind,len(nums)):
            res.append(nums[i])
        for i in range(ind):
            res.append(nums[i])
        for i in range(len(nums)):
            nums[i]=res[i]