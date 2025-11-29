class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        from collections import Counter
        
        total_chars = sum(len(word) for word in words)
        n = len(words)
        
        if total_chars % n != 0:
            return False
        
        freq = Counter()
        for word in words:
            freq.update(word)
        
        for count in freq.values():
            if count % n != 0:
                return False
        
        return True
