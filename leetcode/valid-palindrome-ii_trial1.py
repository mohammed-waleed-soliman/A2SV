class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        while i<=j:
            if s[i]!=s[j]:
                break
            i+=1
            j-=1
        if i>j:
            return True
        x = i
        y = j-1
        while x<=y:
            if s[x]!=s[y]:
                break
            x+=1
            y-=1
        if x>y:
            return True
        x = i+1
        y = j
        while x<=y:
            if s[x]!=s[y]:
                break
            x+=1
            y-=1
        if x>y:
            return True
        return False