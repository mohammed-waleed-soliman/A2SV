class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        v = ["a","e","o","u","i"]
        mp = dict()
        mp["a"]=0
        mp["e"]=0
        mp["o"]=0
        mp["u"]=0
        mp["i"]=0
        for i in range(k):
            if s[i] in mp:
                mp[s[i]]+=1
        res = 0
        for h in range(5):
            res += mp[v[h]]
        i = 0
        j = k
        while j<len(s):
            if s[j] in mp:
                mp[s[j]]+=1
            if s[i] in mp:
                mp[s[i]]-=1
            j+=1
            i+=1
            temp = 0
            for h in range(5):
                temp += mp[v[h]]
            res = max(res,temp)
        return res