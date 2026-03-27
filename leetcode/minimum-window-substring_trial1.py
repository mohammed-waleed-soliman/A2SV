class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""
        map = [0]*128
        for i in t:
            map[ord(i)]+=1
        count=len(t)
        i=0
        j=0
        mn=1000000000
        ind=0
        while j<len(s):
            if map[ord(s[j])]>0:
                count-=1
            map[ord(s[j])]-=1
            j+=1
            while count==0:
                if j-i<mn:
                    ind=i
                    mn=j-i
                if map[ord(s[i])]==0:
                    count+=1
                map[ord(s[i])]+=1
                i+=1
        if mn==1000000000:
            return ""
        else:
            return s[ind:ind + mn]