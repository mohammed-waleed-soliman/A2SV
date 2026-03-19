class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        pre=[0]*(len(nums)+1)
        for i in range(len(nums)):
            pre[i+1]=pre[i]+nums[i]
        mp=dict()
        for i in range(len(nums)+1):
            if (pre[i]%k) in mp:
                mp[pre[i]%k].append(i)
            else:
                mp[pre[i]%k]=[i]
        for key in mp:
            if mp[key][-1]-mp[key][0]>1:
                return True
        return False