class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        l = list(range(n))
        last = 0
        ind = 0
        k -= 1
        for i in range(len(l)-1):
            l.remove(l[(ind+k)%len(l)])
            ind = (ind+k)%(len(l)+1)
        return l[0]+1