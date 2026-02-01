class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        from typing import List

        n = len(nums)
        first_cost = nums[0]

        min_left = nums[1]
        min_sum = float('inf')

        for k in range(2, n):
            current_sum = min_left + nums[k]
            if current_sum < min_sum:
                min_sum = current_sum
            if nums[k] < min_left:
                min_left = nums[k]
        
        return first_cost + min_sum
