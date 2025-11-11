class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        heil = 0
        maxi = 0
        
        for g in gain:
            heil += g
            if heil > maxi:
                maxi = heil
        
        return maxi
