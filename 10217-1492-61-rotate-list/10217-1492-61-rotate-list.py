# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        length = 0
        curr = head
        
        while curr:
            curr = curr.next
            length += 1

        if not head or length == 1 or (k%length) == 0:
            return head

        curr = head
        prev = curr

        for i in range(length - (k%length)):
            prev = curr
            curr = curr.next
        
        prev.next = None
        
        new_head = curr
        last = curr

        while curr:
            last = curr
            curr = curr.next
        
        last.next = head

        return new_head