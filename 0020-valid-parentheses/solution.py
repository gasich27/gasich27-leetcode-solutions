class Solution(object):
    def isValid(self, s):
        st = []

        for ch in s:
            if ch == '(' or ch == '[' or ch == '{':
                st.append(ch)
            else:
                if not st:
                    return False

                if (ch == ')' and st[-1] != '(') or \
                   (ch == ']' and st[-1] != '[') or \
                   (ch == '}' and st[-1] != '{'):
                    return False

                st.pop()

        return len(st) == 0
