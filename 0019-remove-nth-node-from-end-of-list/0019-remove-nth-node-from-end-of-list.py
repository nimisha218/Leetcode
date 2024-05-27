# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        slow = head
        fast = head

        if not slow.next:
            if n == 1:
                slow = None
                return slow

        for _ in range(n-1):
            fast = fast.next
        
        while fast and fast.next:
            prev_node = slow
            slow = slow.next
            fast = fast.next
        
        if slow == head:
            return slow.next
        
        if slow and slow.next:
            prev_node.next = slow.next
        else:
            prev_node.next = None

        return head