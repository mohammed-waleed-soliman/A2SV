class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        x = -1
        y = -1
        l = 0
        r = len(nums)-1
        while l<=r:
            mid = l+(r-l)//2
            if nums[mid]>target:
                r = mid-1
            elif nums[mid]<target:
                l = mid+1
            else:
                x = mid
                r = mid-1
        l = 0
        r = len(nums)-1
        while l<=r:
            mid = l+(r-l)//2
            if nums[mid]>target:
                r = mid-1
            elif nums[mid]<target:
                l = mid+1
            else:
                y = mid
                l = mid+1
        return [x,y]