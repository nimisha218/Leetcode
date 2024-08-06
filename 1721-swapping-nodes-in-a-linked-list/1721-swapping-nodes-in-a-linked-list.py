# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        prev = dummy

        slow = head
        fast = head
        p1 = p2 = head

        for _ in range(k-1):
            fast = fast.next
            p1 = fast
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next

        p2 = slow

        p1.val, p2.val = p2.val, p1.val

        return dummy.next