class Solution:
    def minOperations(self, logs: List[str]) -> int:
        res = 0
        for i in range(len(logs)):
            if logs[i]=="../":
                res=max(res-1,0)
            elif logs[i][0]!='.':
                res+=1
        return res