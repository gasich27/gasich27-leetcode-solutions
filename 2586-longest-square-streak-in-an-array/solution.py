class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums_set = set(nums)
        ans = -1

        for x in nums_set:
            length = 0
            cur = x

            while cur in nums_set:
                length += 1
                cur = cur * cur

                if cur > 10**5 * 10**5:
                    break

            if length >= 2:
                ans = max(ans, length)

        return ans
