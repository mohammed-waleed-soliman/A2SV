class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [[1]]
        rowIndex+=1
        if rowIndex==1:
            return res[0]
        for i in range(1,rowIndex):
            temp = [1]
            for j in range(i-1):
                temp.append(res[i-1][j+1]+res[i-1][j])
            temp.append(1)
            res.append(temp)
        return res[-1]