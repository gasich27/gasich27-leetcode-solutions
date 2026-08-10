class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicst = {}
        n = len(nums)

        for i in range(n):
            comp = target - nums[i]
            if comp in dicst:
                return [dicst[comp], i]
            else:
                dicst[nums[i]] = i


        
