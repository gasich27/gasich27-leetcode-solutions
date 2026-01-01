class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        lst = []

        for x in nums:
            heapq.heappush(lst, x)

            if len(lst) > k:
                heapq.heappop(lst)
            
        return lst[0]
