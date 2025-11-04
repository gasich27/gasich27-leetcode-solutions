class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        flowerbed = [0] + flowerbed + [0]
        count = 0
        possible = 0
        
        for plot in flowerbed:
            if plot == 0:
                count += 1
            else:
                if count > 0:
                    possible += (count - 1) // 2
                    count = 0
        if count > 0:
            possible += (count - 1) // 2
        
        return possible >= n

