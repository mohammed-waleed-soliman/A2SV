class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        for val in set(s):
            i = 0
            count = 0
            for j in range(len(s)):
                if s[j]!=val:
                    count+=1
                while count>k:
                    if s[i]!=val:
                        count-=1
                    i+=1
                res=max(res,j-i+1)
        return res      