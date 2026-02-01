class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(pos: int):
            if pos == len(nums):
                res.append(nums[:])
                return

            for i in range(pos, len(nums)):
                nums[pos], nums[i] = nums[i], nums[pos]
                dfs(pos + 1)
                nums[pos], nums[i] = nums[i], nums[pos]

        dfs(0)
        return res
