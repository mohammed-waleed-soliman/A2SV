class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        res = 0
        j = 0
        g.sort()
        s.sort()
        for i in range(len(g)):
            if j>=len(s):
                break
            while g[i]>s[j]:
                j+=1
                if j==len(s):
                    return res
            res+=1
            j+=1
        return res