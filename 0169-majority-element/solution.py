class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        lst = {}

        for i in nums:
            if i not in lst:
                lst[i] = 1
            elif i in lst:
                lst[i] += 1
        return max(lst, key=lst.get)
