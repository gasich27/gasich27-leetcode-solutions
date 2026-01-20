class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        n, m = len(spells), len(potions)
        result = []
        
        for spell in spells:
            min_potion = (success + spell - 1) // spell 
            idx = bisect_left(potions, min_potion)
            result.append(m - idx) 

        return result
