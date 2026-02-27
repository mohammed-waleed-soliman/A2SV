class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        steps = len(piles)//3
        res = 0
        for i in range(1,steps*2+1,2):
            res += piles[i]
        return res