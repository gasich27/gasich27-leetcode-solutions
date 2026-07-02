class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        sl = {}
        for i in nums:
            if i in sl and sl[i] >= 1:
                return True 
            sl[i] = sl.get(i, 0) + 1
        return False
