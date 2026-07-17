class Solution:
    def checkValidString(self, s: str) -> bool:
        maxi = mini = 0 
        for c in s:
            if c == '(':
                maxi += 1
                mini += 1
            if c == ')':
                maxi -= 1
                mini = max(mini - 1, 0)
            if c == '*':
                maxi += 1
                mini = max(mini - 1, 0)
            if maxi < 0:
                return False
        return mini == 0
