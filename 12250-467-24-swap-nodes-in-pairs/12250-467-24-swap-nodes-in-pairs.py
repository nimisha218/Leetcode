# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        prev = dummy

        while prev.next and prev.next.next:
            
            first = prev.next
            second = prev.next.next

            first.next = second.next
            second.next = first
            prev.next = second

            prev = first
        
        return dummy.next

        

        
        # # # Recursive solution
        # # if not head or not head.next:
        # #     return head
        
        # # nxt = head.next
        # # head.next = self.swapPairs(head.next.next)
        # # nxt.next = head
        # # return nxt

        # # Iterative solution
        # dummy = ListNode(0, head)
        # prev = dummy

        # # Check if we have a pair
        # while prev.next and prev.next.next:

        #     firstNode = prev.next
        #     secondNode = prev.next.next

        #     firstNode.next = secondNode.next
        #     secondNode.next = firstNode
        #     prev.next = secondNode

        #     prev = firstNode
        
        # return dummy.next




