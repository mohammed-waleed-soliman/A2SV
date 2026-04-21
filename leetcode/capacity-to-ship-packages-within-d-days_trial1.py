class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        res = r
        while l<=r:
            mid = l+(r-l)//2
            count = 0
            s = 0
            for i in range(len(weights)):
                if s+weights[i]<=mid:
                    s+=weights[i]
                else:
                    count+=1
                    s=weights[i]
            if s!=0:
                count+=1
            if count>days:
                l = mid+1
            else:
                res = mid
                r = mid-1
        return res