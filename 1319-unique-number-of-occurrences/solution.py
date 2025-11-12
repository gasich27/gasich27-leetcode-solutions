class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        slova = {}
        uniq = []
        
        for i in range(len(arr)):
            if arr[i] in slova:
                slova[arr[i]] += 1
            else:
                slova[arr[i]] = 1
        
        for u, v in slova.items():
            if v in uniq:
                return False
            else:
                uniq.append(v)
        return True
