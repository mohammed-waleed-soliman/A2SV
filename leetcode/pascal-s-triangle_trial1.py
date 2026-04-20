class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        if numRows==1:
            return res
        for i in range(1,numRows):
            temp = [1]
            for j in range(i-1):
                temp.append(res[i-1][j+1]+res[i-1][j])
            temp.append(1)
            res.append(temp)
        return res