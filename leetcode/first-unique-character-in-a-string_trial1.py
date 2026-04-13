class Solution:
    def firstUniqChar(self, s: str) -> int:
        mp = dict()
        for i in range(len(s)):
            if s[i] not in mp:
                mp[s[i]] = [i]
            else:
                mp[s[i]].append(i)
        for i in range(len(s)):
            if len(mp[s[i]])==1:
                return i
        return -1