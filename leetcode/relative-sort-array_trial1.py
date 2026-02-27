class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        mp = dict()
        mn = 100000
        mx = -1
        for i in range(len(arr1)):
            mn = min(mn,arr1[i])
            mx = max(mx,arr1[i])
            if arr1[i] in mp:
                mp[arr1[i]] += 1
            else:
                mp[arr1[i]] = 1
        res = []
        for i in range(len(arr2)):
            while mp[arr2[i]]:
                res.append(arr2[i])
                mp[arr2[i]] -= 1
        for i in range(mn,mx+1):
            if i not in mp:
                continue
            while mp[i]:
                res.append(i)
                mp[i] -= 1
        return res