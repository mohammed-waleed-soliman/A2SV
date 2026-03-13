class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        j = len(cardPoints)-k
        s = 0
        total = sum(cardPoints)
        for i in range(j):
            s += cardPoints[i]
        mn = s
        i = 0
        while j<len(cardPoints):
            s += cardPoints[j]
            s -= cardPoints[i]
            i+=1
            j+=1
            mn = min(mn,s)
        return total-mn