class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i = 0
        j = 0
        n = len(firstList)
        m = len(secondList)
        res = []
        while i<n and j<m:
            if firstList[i][1]<secondList[j][0]:
                i+=1
            elif firstList[i][0]>secondList[j][1]:
                j+=1
            else:
                if firstList[i][1]<=secondList[j][1]:
                    res.append([max(firstList[i][0],secondList[j][0]),firstList[i][1]])
                else:
                    res.append([max(firstList[i][0],secondList[j][0]),secondList[j][1]])
                if firstList[i][1]>secondList[j][1]:
                    j+=1
                else:
                    i+=1
        return res