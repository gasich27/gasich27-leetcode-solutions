class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxi = 0
        left = 0
        right = len(height) - 1

        while left < right:
            s = (right - left) * min(height[left], height[right])
            maxi = max(maxi, s)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
    
        return maxi
        
