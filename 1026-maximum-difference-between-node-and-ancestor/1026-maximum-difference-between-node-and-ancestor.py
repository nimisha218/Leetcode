# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        def dfs(node, currMin, currMax):

            if not node:
                return

            if node.val > currMax:
                currMax = node.val
            if node.val < currMin:
                currMin = node.val
            
            # Check for the current difference
            if abs(node.val - currMin) >= result[0]:
                result[0] = abs(node.val - currMin)
            if abs(node.val - currMax) >= result[0]:
                result[0] = abs(node.val - currMax)
            
            if node.left:
                dfs(node.left, currMin, currMax)
            if node.right:
                dfs(node.right, currMin, currMax)
        
        result = [float('-inf')]

        dfs(root, float('inf'), float('-inf'))

        return result[0] if result[0] != float('-inf') else 0


            