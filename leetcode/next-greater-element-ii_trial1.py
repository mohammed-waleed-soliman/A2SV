class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        mx = max(nums)
        res = [-1]*len(nums)
        temp = []
        for i in nums: temp.append(i)
        for i in nums: temp.append(i)
        j = 0
        st = []
        while j < len(temp):
            while len(st):
                if temp[j]>st[-1][0]:
                    res[st[-1][1]%len(nums)] = nums[j%len(nums)]
                    st.pop()
                else:
                    break
            st.append([nums[j%len(nums)],j])
            j+=1
        return res