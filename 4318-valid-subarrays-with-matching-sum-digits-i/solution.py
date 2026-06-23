class Solution:
    def countValidSubarrays(self, nums: list[int], x: int) -> int:
        n = len(nums)

        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]

        ans = 0

        for l in range(n):
            for r in range(l, n):
                s = pref[r + 1] - pref[l]

                if s % 10 != x:
                    continue

                first = s
                while first >= 10:
                    first //= 10

                if first == x:
                    ans += 1

        return ans
