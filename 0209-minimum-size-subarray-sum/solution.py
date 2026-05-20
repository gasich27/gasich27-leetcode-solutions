class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        cur = 0 
        min_len = float('inf')

        for right in range(n):
            cur += nums[right]

            while cur >= target:
                min_len = min(min_len, right - left + 1)
                cur -= nums[left]
                left += 1
    
        return min_len if min_len != float('inf') else 0

