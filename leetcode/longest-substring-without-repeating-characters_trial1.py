class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 1
        mp = dict()
        if len(s)==0:
            return 0
        mp[s[i]]=1
        res = 1
        while j<len(s):
            if s[j] in mp:
                mp[s[j]]+=1
            else:
                mp[s[j]]=1
            while mp[s[j]]>1:
                mp[s[i]]-=1
                i+=1
            res = max(res,j-i+1)
            j+=1
        return res