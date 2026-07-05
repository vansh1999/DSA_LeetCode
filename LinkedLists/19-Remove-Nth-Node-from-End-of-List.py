# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        d = ListNode()
        d.next = head
        a = b = d

        # Put a at n + 1 position at start
        for i in range(n+1):
            a = a.next

        # move a and b till a is out of balance / none
        while a:
            a = a.next
            b = b.next

        b.next = b.next.next

        # dont return head for edge case when n is the first node, so do d
        return d.next