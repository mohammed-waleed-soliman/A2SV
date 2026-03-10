class Solution:
    def compress(self, chars: List[str]) -> int:
        temp=[]
        x = 1
        for i in range(1,len(chars)):
            if chars[i]==chars[i-1]:
                x+=1
            elif x>1:
                word = str(x)
                n = len(word)
                temp.append(chars[i-1])
                for j in range(n):
                    temp.append(word[j])
                x = 1
            else:
                temp.append(chars[i-1])
                x = 1
        temp.append(chars[len(chars)-1])
        if x>1:
            word = str(x)
            n = len(word)
            for j in range(n):
                temp.append(word[j])
        for i in range(len(temp)):
            chars[i]=temp[i]
        return len(temp)