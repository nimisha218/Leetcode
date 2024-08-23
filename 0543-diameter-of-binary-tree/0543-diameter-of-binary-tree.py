# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):

            if not node:
                return 0
            
            if node.left == None and node.right == None:
                # We are at a leaf node
                return 0
            
            # We are not at a leaf node
            # Need to compute the left height and the right height
            left = None
            if node.left:
                left = 1 + dfs(node.left)   
            right = None
            if node.right:
                right = 1 + dfs(node.right)
        
            if left and right:
                # Potentially update the result
                result[0] = max(result[0], left + right, left, right)
                return max(left, right)
            elif left:
                result[0] = max(result[0], left)
                return left
            elif right:
                result[0] = max(result[0], right)
                return right
        
        result = [float('-inf')]
        
        dfs(root)

        return result[0] if result[0] != float(-inf) else 0
            
            
            
            

            

            

        

            
            

            
            