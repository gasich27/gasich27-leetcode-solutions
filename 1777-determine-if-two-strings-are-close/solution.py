class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        w1, w2 = {}, {}
    
        if len(word1) != len(word2):
            return False

        for i in word1:
            w1[i] = w1.get(i, 0) + 1
        for j in word2:
            w2[j] = w2.get(j, 0) + 1

        if set(w1.keys()) != set(w2.keys()):
            return False

        return sorted(w1.values()) == sorted(w2.values())
