# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Find the middle node
        slow = head
        fast = head

        if not slow.next:
            return None

        while fast and fast.next:
            prev_node = slow
            slow = slow.next
            fast = fast.next.next

        if slow.next:
            next_node = slow.next
            prev_node.next = next_node
        else:
            prev_node.next = None
        
        return head