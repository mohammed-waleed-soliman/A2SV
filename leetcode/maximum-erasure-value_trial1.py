class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        freq=[0]*(max(nums)+1)
        print(freq)
        freq[nums[0]]+=1
        i=0
        j=1
        s=nums[0]
        res=s
        while j<len(nums):
            s+=nums[j]
            freq[nums[j]]+=1
            while freq[nums[j]]>1:
                s-=nums[i]
                freq[nums[i]]-=1
                i+=1
            res = max(res,s)
            j+=1
        return res