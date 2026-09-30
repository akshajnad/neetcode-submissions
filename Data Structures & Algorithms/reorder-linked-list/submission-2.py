# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        curr = second
        slow.next = None
        prev = None
        nex = second.next
        while nex:
            curr.next = prev
            prev = curr
            curr = nex
            nex = nex.next
        curr.next = prev
        t = curr
        h = head
        while t:
            headnext, tailnext = h.next, t.next
            h.next = t
            t.next = headnext
            h = headnext
            t = tailnext
        
        

