# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        def mergeLists(l1, l2):

            dummy = ListNode()
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
        
        if len(lists) == 0:
            return None
        
        if len(lists) == 1:
            return lists[0]

        while len(lists) > 1:

            merged = []

            l1 = lists.pop()
            l2 = lists.pop()

            merged = mergeLists(l1, l2)

            lists.append(merged)
        
        return lists[0]
