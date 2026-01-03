class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = sorted(zip(nums2, nums1), reverse=True)
        
        heap = []
        heap_sum = 0
        ans = 0
        
        for b, a in pairs:
            heapq.heappush(heap, a)
            heap_sum += a
            
            if len(heap) > k:
                heap_sum -= heapq.heappop(heap)
            
            if len(heap) == k:
                ans = max(ans, heap_sum * b)
        
        return ans


