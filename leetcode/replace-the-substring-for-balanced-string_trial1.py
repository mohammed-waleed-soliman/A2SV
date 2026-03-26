class Solution:
    def balancedString(self, s: str) -> int:
        i = 0
        res = len(s)
        count = Counter(s)
        for right in range(len(s)):
            count[s[right]] -= 1
            while i<len(s) and 4*max(count.values())<=len(s):
                res = min(res,right-i+1)
                count[s[i]]+=1 
                i+=1
        return res
