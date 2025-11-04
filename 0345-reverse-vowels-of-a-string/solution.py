class Solution(object):
    def reverseVowels(self, s):
        vowels = set('AEIOUaeiou')
        s = list(s)
        r1 = 0
        r2 = len(s)-1
        
        while r1 < r2:
            if s[r1] not in vowels:
                r1 += 1
            elif s[r2] not in vowels:
                r2 -= 1
            else:
                s[r1], s[r2] = s[r2], s[r1]
                r1 += 1
                r2 -= 1
        return ''.join(s)
        
