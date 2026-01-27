class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        ops = {"+", "-", "*", "/"}

        for t in tokens:
            if t not in ops:
                st.append(int(t))
            else:
                b = st.pop()
                a = st.pop()

                if t == "+":
                    st.append(a + b)
                elif t == "-":
                    st.append(a - b)
                elif t == "*":
                    st.append(a * b)
                else:  # "/"
                    st.append(int(a / b))  # truncate toward 0

        return st[-1]

