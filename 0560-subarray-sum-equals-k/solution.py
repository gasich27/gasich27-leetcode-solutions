class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0
        count = 0

        freq = [0]*(1000)*len(nums)
        freq[0] = 1

        for x in nums:
            prefix += x

            count += freq[prefix - k]

            freq[prefix] += 1

        return count
