class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        pre=[0]*(len(s)+2)
        for i in range(len(shifts)):
            if shifts[i][2]==0:
                pre[shifts[i][0]+1]-=1
                pre[shifts[i][1]+2]+=1
            else:
                pre[shifts[i][0]+1]+=1
                pre[shifts[i][1]+2]-=1
        for i in range(1,len(pre)):
            pre[i]+=pre[i-1]
        for i in range(0,len(pre)):
            pre[i] = ((pre[i]%26)+26)%26
        res = []
        for i in range(len(s)):
            res.append(chr(((ord(s[i])-ord('a')+pre[i+1])%26)+ord(('a'))))
        print(res)
        return "".join(res)
        