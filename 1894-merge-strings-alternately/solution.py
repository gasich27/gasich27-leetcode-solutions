class Solution(object):
    def mergeAlternately(self, word1, word2):
        word = ''
        if len(word1) == len(word2):
            for i in range(len(word1)):
                word += word1[i]
                word += word2[i]
    
        elif len(word1) < len(word2):
            for i in range(len(word1)):
                word += word1[i]
                word += word2[i]
            word += word2[len(word1):]
    
        elif len(word1) > len(word2):
            for i in range(len(word2)):
                word += word1[i]
                word += word2[i]
            word += word1[len(word2):]  
    
        return word
       
