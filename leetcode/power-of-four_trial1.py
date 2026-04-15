class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n==0:
            return False
        def p(x: int) -> bool:
            if x==1:
                return True
            if x%4==0:
                return p(x/4)
            else:
                return False
        return p(n)