class Solution(object):
    def gcdOfStrings(self, str1, str2):
        if str1 + str2 != str2 + str1:
            return ''
        else:
            a = len(str1)
            b = len(str2)
        
            while a != 0 and b != 0:
                if a > b:
                    a = a % b
                else:
                    b = b % a
            n = a + b
            return str1[:n]


