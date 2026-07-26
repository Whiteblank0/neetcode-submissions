class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = ['+', '-', '*', '/']
        st = []

        for token in tokens:
            if token not in op:
                st.append(int(token))
            else:
                sec = st.pop()
                fir = st.pop()
                if token == '+':
                    result = fir + sec
                    st.append(result)
                elif token == '-':
                    result = fir - sec
                    st.append(result)
                elif token == '*':
                    result = fir * sec
                    st.append(result)
                elif token == '/':
                    result = int(fir / sec)
                    st.append(result)

        return st[-1] 