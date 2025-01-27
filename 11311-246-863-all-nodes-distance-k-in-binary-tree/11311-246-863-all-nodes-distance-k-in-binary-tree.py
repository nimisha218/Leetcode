# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
from collections import defaultdict

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        # Reconstruct the binary tree to be a graph
        graph = defaultdict(list)

        def dfs(node, parent):

            if not node:
                return
            
            # We have a node
            graph[node.val].append(parent.val)
            graph[parent.val].append(node.val)

            # Go left
            dfs(node.left, node)

            # Go right
            dfs(node.right, node)

        dfs(root, root)

        queue = deque([target.val])

        seen = {target.val}

        if k == 0:
            return [target.val]

        while queue:
            
            num_nodes = len(queue)
            result = []

            for i in range(num_nodes):

                node = queue.popleft()

                for neighbor in graph[node]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        queue.append(neighbor)
                        result.append(neighbor)
                
            k -= 1
            if k == 0:
                return result

        return result
            
            