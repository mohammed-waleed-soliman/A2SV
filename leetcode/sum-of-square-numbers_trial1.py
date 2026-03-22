class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        sq=dict()
        a=0
        while a*a<=c:
            sq[a*a]=True
            a+=1
        a=0
        while a*a<=c:
            if c-(a*a) in sq:
                return True
            a+=1
        return False