class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp=[]
        for i in s:
            if i.isalnum():
                temp.append(i.lower())
        print(temp)
        cond = True
        for i in range(len(temp)//2):
            if temp[i]!=temp[len(temp)-1-i]:
                cond = False
                break
        return cond