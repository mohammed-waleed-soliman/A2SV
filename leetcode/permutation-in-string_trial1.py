class Solution:
    def check(self, a: dict, b: dict) ->bool:
        for i in a:
            if i in b:
                if a[i]!=b[i]:
                    return False
            else:
                return False
        return True
    def checkInclusion(self, s1: str, s2: str) -> bool:
        p=s1
        s=s2
        if len(p)>len(s):
            return False
        mp=dict()
        for i in p:
            if i in mp:
                mp[i]+=1
            else:
                mp[i]=1
        freq=dict()
        for i in range(len(p)):
            if s[i] in freq:
                freq[s[i]]+=1
            else:
                freq[s[i]]=1
        print(freq,mp)
        i = 0
        j = len(p)
        cond = self.check(mp,freq)
        if cond:
            return True
        while j<len(s):
            if s[j] in freq:
                freq[s[j]]+=1
            else:
                freq[s[j]]=1
            freq[s[i]]-=1
            j+=1
            i+=1
            cond = self.check(mp,freq)
            if cond:
                return True
        return False