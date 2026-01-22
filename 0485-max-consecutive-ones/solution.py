class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        ser = 0
        for i in nums:
            if i == 1:
                ser += 1
            if i == 0:
                ser = 0
            if ser > res:
                res = ser
        return res
