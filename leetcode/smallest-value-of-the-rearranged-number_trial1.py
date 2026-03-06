class Solution:
    def smallestNumber(self, num: int) -> int:
        if num<0:
            num *= -1
            word = str(num)
            mp = dict()
            for i in range(len(word)):
                if ord(word[i])-ord('0') in mp:
                    mp[ord(word[i])-ord('0')] += 1
                else:
                    mp[ord(word[i])-ord('0')] = 1
            res = 0
            for i in range(9,-1,-1):
                if i in mp:
                    for j in range(mp[i]):
                        res *= 10
                        res += i
            num=res*-1
        else:
            word=str(num)
            mp = dict()
            for i in range(len(word)):
                if ord(word[i])-ord('0') in mp:
                    mp[ord(word[i])-ord('0')] += 1
                else:
                    mp[ord(word[i])-ord('0')] = 1
            res = 0
            for i in range(1,10):
                if i in mp:
                    res = i
                    mp[i]-=1
                    break
            for i in range(10):
                if i in mp:
                    for j in range(mp[i]):
                        res *= 10
                        res += i
            num=res
        return num