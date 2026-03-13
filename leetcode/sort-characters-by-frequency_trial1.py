class Solution:
    def frequencySort(self, s: str) -> str:
        if len(s)=="":
            return ""
        mp = dict()
        mx = 0
        for i in s:
            if i in mp:
                mp[i]+=1
            else:
                mp[i]=1
        res = []
        mx = 1
        while mx!=0:
            mx = 0
            temp = "a"
            for i in mp:
                if mp[i]>=mx:
                    mx = mp[i]
                    temp = i
            if mx!=0:
                while mp[temp]!=0:
                    res.append(temp)
                    mp[temp]-=1
        return "".join(res)