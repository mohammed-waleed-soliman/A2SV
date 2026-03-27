class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        mp=defaultdict(int)
        count=0
        res=0
        i=0
        for j in range(len(nums)):
            count+=mp[nums[j]]
            mp[nums[j]]+=1
            while count>=k:
                res+=len(nums)-j
                count-=mp[nums[i]]-1
                mp[nums[i]]-=1
                i+=1
        return res