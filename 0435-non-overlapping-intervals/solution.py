class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])

        end = -inf
        k = 0

        for v, u in intervals:
            if v >= end:
                end = u
            else:
                k += 1
        
        return k
