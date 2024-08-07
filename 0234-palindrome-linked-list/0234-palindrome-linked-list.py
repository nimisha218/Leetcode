# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

    
        dummy = ListNode(0, head)

        slow = fast = head
        p1 = head
        p2_prev = dummy
        c1 = 0

        while fast and fast.next:
            p2_prev = slow
            slow = slow.next
            c1 += 1
            fast = fast.next.next

        p2 = slow

        prev = None
        c2 = 0

        while p2:
            c2 += 1
            n = p2.next
            p2.next = prev
            prev = p2
            p2 = n
        
        p2_prev.next = prev

        p1 = dummy.next
        p2 = prev

        if c1 == c2:
            while p1 and p2:
                if p1.val != p2.val:
                    return False
                p1 = p1.next
                p2 = p2.next
        
        else:
            while p1 and p2 and p2.next:
                if p1.val != p2.val:
                    return False
                p1 = p1.next
                p2 = p2.next
    
        return True
        