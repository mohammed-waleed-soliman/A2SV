class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        v = ["a","e","o","u","i"]
        mp = dict()
        mp["a"]=0
        mp["e"]=0
        mp["o"]=0
        mp["u"]=0
        mp["i"]=0
        res = 0
        n = len(word)
        for i in range(n):
            if word[i] in v:
                for j in range(i,n):
                    if word[j] in v:
                        mp[word[j]]+=1
                        count = 0
                        for k in range(5):
                            if mp[v[k]]!=0:
                                count+=1
                        if count==5:
                            res+=1
                    else:
                        break
                for k in range(5):
                    mp[v[k]]=0
        return res