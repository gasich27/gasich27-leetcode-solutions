class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        
        for i in range(1, n+1):
            if nums.count(i) == 2:
                res.append(i)
                break
        for i in range(1, n+1):
            if i not in nums:
                res.append(i)
    
        return res


