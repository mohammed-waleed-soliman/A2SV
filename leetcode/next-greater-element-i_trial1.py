class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st = []
        mp = dict()
        j = 0
        while j<len(nums2):
            while len(st):
                if nums2[j]>st[-1]:
                    mp[st[-1]]=j
                    st.pop()
                else:
                    break
            st.append(nums2[j])
            j+=1
        res = []
        for i in nums1:
            if i in mp:
                res.append(nums2[mp[i]])
            else:
                res.append(-1)
        return res