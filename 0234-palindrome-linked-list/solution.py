# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        cur = slow
        prev = None

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        sec = prev

        fir = head
        secd = sec
        while secd:
            if fir.val != secd.val:
                return False
            fir = fir.next
            secd = secd.next
            
        return True
