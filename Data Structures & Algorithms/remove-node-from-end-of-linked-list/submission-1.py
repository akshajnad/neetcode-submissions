# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        if not head.next and n == 1:
            return None
        length = 0
        curr = head
        while curr:
            curr = curr.next
            length += 1
        if n == length:
            return head.next
        curr = head
        i = 0
        while i < length - n - 1:
            curr = curr.next
            i += 1
        curr.next = curr.next.next
        return head
