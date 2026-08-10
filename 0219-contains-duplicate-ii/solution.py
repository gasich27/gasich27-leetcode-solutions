class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dist = {}

        for i, val in enumerate(nums):
            if val in dist and i - dist[val] <= k:
                return True
            else:
                dist[val] = i

        return False
