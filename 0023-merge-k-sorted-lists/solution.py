# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        import heapq

        minHeap = []

        for i, node in enumerate(lists):
            if node:
                minHeap.append((node.val, i, node))
        heapq.heapify(minHeap)

        dummy = prev = ListNode(0)
        while minHeap:
            _, i, node = heapq.heappop(minHeap)
            prev.next = node
            prev = prev.next
            if node.next:
                heapq.heappush(minHeap, (node.next.val, i, node.next))
        
        return dummy.next

