class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count=0
        for i in range(len(nums)):
            if nums[i]==0:
                count+=1
        if count>1:
            return ([0]*len(nums))
        if count==1:
            res=[0]*len(nums)
            ind = 0
            x = 1
            for i in range(len(nums)):
                if nums[i]==0:
                    ind = i
                else:
                    x *= nums[i]
            res[ind]=x
            return res
        else:
            x = 1
            for i in range(len(nums)):
                x *= nums[i]
            res=[]
            for i in range(len(nums)):
                res.append(x//nums[i])
            return res