class Solution:
    def minOperations(self, nums: List[int]) -> int:
        i=0
        mx=0
        s=sorted(set(nums))
        for j in range(len(s)):
            while s[j]-s[i]>=(len(nums)):
                i+=1
            mx=max(mx,j-i+1)
        return len(nums)-mx