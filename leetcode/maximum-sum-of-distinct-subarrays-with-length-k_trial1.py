class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        mp = defaultdict(int)
        total = 0
        res = 0
        i = 0
        j = 0
        n = len(nums)
        while j<n:
            total+=nums[j]
            mp[nums[j]]+=1
            while mp[nums[j]]>1:
                total-=nums[i]
                mp[nums[i]]-=1
                i+=1
            j+=1
            if j-i==k:
                res = max(res,total)
                total-=nums[i]
                mp[nums[i]]-=1
                i+=1
        return res