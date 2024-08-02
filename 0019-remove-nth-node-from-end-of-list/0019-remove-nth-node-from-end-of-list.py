# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    
        dummy = ListNode(0, head)
        prev = dummy
        slow = head
        fast = head

        for _ in range(n-1):
            fast = fast.next
            
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next

        if prev.next:
            prev.next = prev.next.next
            return dummy.next
        else:
            return None
