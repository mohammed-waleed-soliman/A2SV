class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        res = []
        for i in range(len(arr)):
            if arr[i]!=0:
                res.append(arr[i])
            else:
                res.append(arr[i])
                if(len(res)==len(arr)):
                    break
                res.append(arr[i])
            if(len(res)==len(arr)):
                break
        for i in range(len(arr)):
            arr[i]=res[i]