class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        w=0
        for i in range(k):
            if blocks[i]=='W':
                w+=1
        i=0
        j=k
        mn=w
        while j<len(blocks):
            if blocks[j]=='W':
                w+=1
            if blocks[i]=='W':
                w-=1
            j+=1
            i+=1
            mn = min(mn,w)
        return mn