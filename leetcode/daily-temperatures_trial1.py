class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        res = [0]*len(temperatures)
        j = 0
        while j < len(temperatures):
            while len(st):
                if temperatures[j]>st[-1][0]:
                    res[st[-1][1]]=j-st[-1][1]
                    st.pop()
                else:
                    break
            st.append([temperatures[j],j])
            j+=1
        return res