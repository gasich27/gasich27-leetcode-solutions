class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums11, nums22 = set(nums1), set(nums2)
        res = []
        w1, w2 = [], []
        
        for i in nums11:
            if i not in nums22:
                w1.append(i)
        
        for j in nums22:
            if j not in nums11:
                w2.append(j)

        res.append(w1)
        res.append(w2)
        return res
