class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n==1:
            return 0
        def rec(n: int, k: int, cond: bool) -> int:
            if n==2:
                if cond:
                    return int(not k)
                return k
            a = k%(2**(n-2))
            if k>a:
                return rec(n-1,a,not cond)
            else:
                return rec(n-1,a,cond)
        return rec(n,k-1,False)