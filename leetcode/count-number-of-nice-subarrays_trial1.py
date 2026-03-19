class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        ind=[]
        for i in range(len(nums)):
            if nums[i]%2==1:
                ind.append(i)
        res = 0
        i = 0
        j = k-1
        while j<len(ind):
            before=0
            if i==0:
                before=ind[i]
            else:
                before=ind[i]-ind[i-1]-1
            after=0
            if j==len(ind)-1:
                after=len(nums)-ind[j]-1
            else:
                after=ind[j+1]-ind[j]-1
            i+=1
            j+=1
            res+=1
            res+=before*(after+1)
            res+=after
        return res