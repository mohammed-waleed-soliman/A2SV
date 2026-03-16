class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res=sum(nums[:3])
        for k in range(len(nums)-2):
            req=target-nums[k]
            i=k+1
            j=len(nums)-1
            while i<j:
                if abs(target-res)>abs(target-(nums[k]+nums[i]+nums[j])):
                    res=nums[i]+nums[j]+nums[k]
                if nums[i]+nums[j]>req:
                    j-=1
                else:
                    i+=1
        return res