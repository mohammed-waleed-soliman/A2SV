class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        temp = []
        for i in range(len(nums)):
            j = i+1
            k = len(nums)-1
            while j<k:
                cond = False
                if nums[i]+nums[j]+nums[k]<0:
                    j+=1
                elif nums[i]+nums[j]+nums[k]>0:
                    k-=1
                else:
                    temp.append([nums[i],nums[j],nums[k]])
                    cond = True
                    j+=1
                if j<k:
                    if nums[j]==nums[k] and cond:
                        break
        temp.sort()
        res=[]
        for i in range(len(temp)):
            if i!=0:
                if temp[i][0]!=temp[i-1][0] or temp[i][1]!=temp[i-1][1] or temp[i][2]!=temp[i-1][2]:
                    res.append(temp[i])
            else:
                res.append(temp[i])
        return res