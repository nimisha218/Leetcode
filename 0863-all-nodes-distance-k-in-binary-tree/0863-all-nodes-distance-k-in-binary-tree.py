# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        # Define a recursive dfs method to construct the parent-child heirarchy
        def dfs(node, parent):
            if not node:
                return
            node.parent = parent
            dfs(node.left, node)
            dfs(node.right, node)
        
        dfs(root, None)

        queue = deque([target])
        seen = {target}
        distance = 0
        result = [target.val]
      
        while queue and distance < k:
            curr_neighbors = len(queue)
            result = []
            for i in range(curr_neighbors):
                node = queue.popleft()
                for neighbor in [node.left, node.right, node.parent]:
                    if neighbor and neighbor not in seen:
                        result.append(neighbor.val)
                        seen.add(neighbor)
                        queue.append(neighbor)
            distance += 1

        return result