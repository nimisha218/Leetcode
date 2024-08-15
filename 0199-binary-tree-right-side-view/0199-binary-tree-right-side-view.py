# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []

        queue = deque([root])

        result = []

        while queue:

            num_nodes = len(queue)
            result.append(queue[-1].val)

            for _ in range(num_nodes):

                node = queue.popleft()

                if node.left:
                    queue.append((node.left))
                if node.right:
                    queue.append((node.right))
        
        return result







