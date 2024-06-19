# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root):

            if not root:
                return 0
            
            if not root.left and not root.right:
                return 1
            
            if root.left:
                left = 1 + dfs(root.left)
            else:
                left = None
    
            if root.right:
                right = 1 + dfs(root.right)
            else:
                right = None
    
            if left and right:
                return min(left, right)
            
            if left:
                return left
            
            return right
        
        return dfs(root)
        
