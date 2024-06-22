# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        # Phase 1 -> Get to the left pointer
        dummy = ListNode(0, head)
        leftPrev, curr = dummy, head

        for i in range(left - 1):
            leftPrev = curr
            curr = curr.next
        
        # Phase 2 -> Reverse the left to right chunk of the LL
        prev = None
        for i in range(right - left + 1):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        # Phase 3 -> Modify the final pointers
        leftPrev.next.next = curr
        leftPrev.next = prev

        return dummy.next

