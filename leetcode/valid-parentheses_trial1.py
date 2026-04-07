class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        for i in range(len(s)):
            if s[i]=='(' or s[i]=='[' or s[i]=='{':
                l.append(s[i])
            elif len(l)==0:
                return False
            else:
                if s[i]==')' and l[-1]=='(':
                    l.pop()
                elif s[i]==']' and l[-1]=='[':
                    l.pop()
                elif s[i]=='}' and l[-1]=='{':
                    l.pop()
                else:
                    return False
        if len(l):
            return False
        return True