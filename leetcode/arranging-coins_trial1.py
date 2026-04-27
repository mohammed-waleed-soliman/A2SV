class Solution:
    def arrangeCoins(self, n: int) -> int:
        l = 1
        r = n
        res = 1
        while l<=r:
            mid = l+(r-l)//2
            req = mid*(mid+1)//2
            if req<=n:
                res = mid
                l = mid+1
            else:
                r = mid-1
        return res