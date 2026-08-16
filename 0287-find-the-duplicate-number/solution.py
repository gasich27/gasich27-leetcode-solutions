class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left = 1
        right = len(nums)-1

        while left < right:
            mid = (right+left)//2
            count = 0
            for n in nums:
                if n <= mid:
                    count += 1
            
            if count > mid:
                right = mid
            else:
                left = mid + 1
        
        return left  
