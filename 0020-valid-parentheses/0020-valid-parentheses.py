class Solution:
    def isValid(self, s: str) -> bool:
        st=[]

        hm= {
            ')': '(',
            '}': '{',
            ']': '['
        }
        for i in s:
            if i in hm:
                if not st or st.pop()!=hm[i]:
                    return False
            else:
                st.append(i)
        return len(st)==0