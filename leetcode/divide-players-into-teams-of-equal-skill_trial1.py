class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n = len(skill)
        ref = skill[0]+skill[n-1]
        cond = True
        res = 0
        for i in range(n//2):
            res += skill[i]*skill[n-i-1]
            if(skill[i]+skill[n-i-1]!=ref):
                cond = False
        if cond:
            return res
        return -1