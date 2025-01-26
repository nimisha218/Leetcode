# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        def dfs(node):

            if not node:
                return
            
            if low <= node.val <= high:
                ans[0] += node.val
            
            # Go left
            if node.val > low:
                dfs(node.left)
            
            # Go right
            if node.val < high:
                dfs(node.right)

        ans = [0]
        dfs(root)
        return ans[0]