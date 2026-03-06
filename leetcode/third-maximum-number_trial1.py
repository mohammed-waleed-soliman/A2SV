class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        st = set(nums)
        l = list(st)
        l.sort()
        if len(l)<=2:
            return l[len(l)-1]
        return l[len(l)-3]