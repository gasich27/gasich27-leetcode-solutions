class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        import heapq
        
        freq = Counter(nums)

        heap = []
        
        for num, i in freq.items():
            heapq.heappush(heap, (i, num))

            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for i, num in heap:
            res.append(num)

        return res
