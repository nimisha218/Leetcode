# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root, maxDepth):

            if not root:
                return 0
            
            left = 1 + dfs(root.left, maxDepth)
            right = 1 + dfs(root.right, maxDepth)

            maxDepth = max(left, right)

            return maxDepth
        
        return dfs(root, 0)