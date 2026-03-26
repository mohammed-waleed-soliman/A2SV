class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        i = 0
        res = 0
        mp = defaultdict(int)
        for j in range(len(fruits)):
            mp[fruits[j]]+=1
            while len(mp)>2:
                mp[fruits[i]]-=1
                if mp[fruits[i]]==0:
                    del mp[fruits[i]]
                i += 1
            res = max(res, j-i+1)
        return res