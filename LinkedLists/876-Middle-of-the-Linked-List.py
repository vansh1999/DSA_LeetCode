# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Logic and code own

        a = head
        curr = head

        # lets find LL lenght

        count = 0
        while curr:
            count = count + 1
            curr = curr.next
            

        for _ in range(count//2):
            a = a.next
        
        return a
        
# Time -> O(n) + O(n/2) -> O(n)
# Space -> O(1)

# faster -> use slow and fast pointers

# slow = head
# fast = head

# while fast and fast.next:
#     slow = slow.next
#     fast = fast.next.next

# return slow