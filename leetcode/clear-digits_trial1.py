class Solution:
    def clearDigits(self, s: str) -> str:
        st = []
        for i in s:
            if len(st)>0:
                if not i.isalpha():
                    if st[-1].isalpha():
                        st.pop()
                    else:
                        st.append(i)
                else:
                    st.append(i)
            else:
                st.append(i)
        return "".join(st)