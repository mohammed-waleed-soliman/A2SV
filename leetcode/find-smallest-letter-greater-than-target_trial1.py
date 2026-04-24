class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l = 0
        r = len(letters)-1
        res = r
        while l<=r:
            mid = (l+r)//2
            if ord(letters[mid])>ord(target):
                res = mid
                r = mid-1
            else:
                l = mid+1
        if ord(letters[res])<=ord(target):
            return letters[0]
        return letters[res]