class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if s[i] != ']':
                stack.append(s[i])
            else:
                words = ''
                while stack[-1] != '[':
                    words = stack.pop() + words
                stack.pop()

                integ = ''
                while stack and stack[-1].isdigit():
                    integ = stack.pop() + integ
                stack.append(int(integ) * words)

        return "".join(stack)
