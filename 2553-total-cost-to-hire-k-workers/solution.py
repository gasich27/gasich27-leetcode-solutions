class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        import heapq

        n = len(costs)
        heap1 = []
        heap2 = []
        res = 0

        l = 0
        r = n - 1

        for _ in range(candidates):
            if l <= r:
                heapq.heappush(heap1, (costs[l], l))
                l += 1

        for _ in range(candidates):
            if l <= r:
                heapq.heappush(heap2, (costs[r], r))
                r -= 1

        for _ in range(k):
            if not heap2 or (heap1 and heap1[0] <= heap2[0]):
                cost, idx = heapq.heappop(heap1)
                res += cost

                if l <= r:
                    heapq.heappush(heap1, (costs[l], l))
                    l += 1
            else:
                cost, idx = heapq.heappop(heap2)
                res += cost

                if l <= r:
                    heapq.heappush(heap2, (costs[r], r))
                    r -= 1

        return res






