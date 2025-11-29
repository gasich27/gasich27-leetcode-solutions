class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        r = sum(nums)
        return  r % k

