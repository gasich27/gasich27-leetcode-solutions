import heapq
from typing import List

class Solution:
    def isPossible(self, target: List[int]) -> bool:
        total = sum(target)
        heap = [-x for x in target]
        heapq.heapify(heap)

        while True:
            max_val = -heapq.heappop(heap)

            if max_val == 1:
                return True

            rest_sum = total - max_val

            if rest_sum == 1:
                return True

            if rest_sum <= 0 or rest_sum >= max_val:
                return False

            old_val = max_val % rest_sum

            if old_val == 0:
                return False

            total = rest_sum + old_val
            heapq.heappush(heap, -old_val)
