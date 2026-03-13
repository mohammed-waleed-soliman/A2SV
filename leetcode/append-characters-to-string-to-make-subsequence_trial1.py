class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        i = 0
        j = 0
        while i<n and j<m:
            while s[i]!=t[j]:
                i+=1
                if i==n:
                    break
            if i<n:
                i+=1
                j+=1
        return m-j