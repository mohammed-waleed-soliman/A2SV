class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        l = []
        for i in range(len(score)):
            l.append([score[i],i])
        l.sort(reverse=True)
        res = ["temp"]*len(score)
        j = 4
        for i in range(len(score)):
            if i == 0:
                res[l[i][1]]="Gold Medal"
            elif i == 1:
                res[l[i][1]]="Silver Medal"
            elif i == 2:
                res[l[i][1]]="Bronze Medal"
            else:
                res[l[i][1]]=f"{j}"
                j+=1
        return res