class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr)==1:
            return 1
        temp=[]
        n=len(arr)
        for i in range(len(arr)-1):
            if arr[i]>arr[i+1]:
                temp.append(1)
            elif arr[i]<arr[i+1]:
                temp.append(0)
            else:
                temp.append(2)
        print(temp)
        temp.append(temp[len(temp)-1])
        res=1
        i = 0
        j = 0
        while j<len(temp):
            if temp[j]==2:
                j+=1
                i=j
                continue
            if i==j:
                res=max(res,2)
                j+=1
                continue
            if temp[j]!=temp[j-1]:
                j+=1
                res=max(res,j-i+1)
            else:
                i=j
                j+=1
        return res