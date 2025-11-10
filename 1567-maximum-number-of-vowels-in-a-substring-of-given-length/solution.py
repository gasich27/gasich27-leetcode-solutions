class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        res = 0
        w = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

        leg = 0
        for i in range(k):
            if s[i] in w:
                leg += 1
        res = leg

        for i in range(k, len(s)):
            if s[i - k] in w:
                leg -= 1
                
            if s[i] in w:
                leg += 1

            if leg > res:
                res = leg
        
        return res
        
