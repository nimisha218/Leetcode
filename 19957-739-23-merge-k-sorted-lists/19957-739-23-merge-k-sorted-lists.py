# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        def mergeList(l1, l2):
            dummy = ListNode(0)
            curr = dummy
            while l1 and l2:
                if l1.val <= l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            if l1:
                curr.next = l1
            if l2:
                curr.next = l2
            return dummy.next
        
        l = lists

        if len(l) == 0:
            return None

        if len(l) == 1:
            return l[0]
        
        while len(l) > 1:

            # Merge merge bby

            l1 = l.pop()
            l2 = l.pop()

            l.append(mergeList(l1, l2))
        
        return l[0]

        



