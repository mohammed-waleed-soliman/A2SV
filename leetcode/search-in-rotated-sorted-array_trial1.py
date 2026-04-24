class Solution:
    def search(self, nums: List[int], target: int) -> int:
        mp = dict()
        for i in range(len(nums)):
            mp[nums[i]]=i
        if target in mp:
            return mp[target]
        return -1