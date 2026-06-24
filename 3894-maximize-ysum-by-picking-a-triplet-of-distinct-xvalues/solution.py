class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        best = {}

        for xi, yi in zip(x, y):
            best[xi] = max(best.get(xi, 0), yi)

        if len(best) < 3:
            return -1

        top3 = sorted(best.values(), reverse=True)[:3]
        return sum(top3)
