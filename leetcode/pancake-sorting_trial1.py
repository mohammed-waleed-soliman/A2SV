class Solution:

    def pancakeSort(self, arr: List[int]) -> List[int]:
        size = len(arr)
        res = []
        for i in range(size,0,-1):
            ind = 0
            for j in range(size):
                if arr[j]==i:
                    ind = j
                    break
            if ind+1==i:
                continue
            ind += 1
            res.append(ind)
            for j in range(ind//2):
                temp = arr[j]
                arr[j] = arr[ind-1-j]
                arr[ind-1-j] = temp
            res.append(i)
            for j in range((i+1)//2):
                temp = arr[j]
                arr[j] = arr[i-1-j]
                arr[i-1-j] = temp
        return res