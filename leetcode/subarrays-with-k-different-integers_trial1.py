class Solution:
    def count(self, nums: List[int], k: int, l: int) -> int:
        res=0
        i=0
        mp=defaultdict(int)
        for j in range(l):
            mp[nums[j]]+=1
            while len(mp)>k:
                mp[nums[i]]-=1
                if mp[nums[i]]==0:
                    del mp[nums[i]]
                i+=1
            res+=j-i+1
        return res
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.count(nums,k,len(nums))-self.count(nums,k-1,len(nums))