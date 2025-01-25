# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(node, curr):

            if not node:
                return False
            
            # Check if a leaf node?
            if not node.left and not node.right:
                return node.val + curr == targetSum
            
            return dfs(node.left, curr + node.val) or dfs(node.right, curr + node.val)
        
        return dfs(root, 0)
            
            