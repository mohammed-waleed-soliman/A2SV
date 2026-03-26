class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        i = 0
        x = 0
        for j in range(1,len(s)):
            x += s[j]==s[j-1]
            if x > 1:
                i+=1
                x-=s[i]==s[i-1]
        return len(s)-i