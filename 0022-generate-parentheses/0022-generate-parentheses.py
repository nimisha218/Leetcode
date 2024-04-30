class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        result = []
        stack = []

        # Define a backtrack method
        def backtrack(openN, closedN):
            
            # Base Case (One of the solutions found)
            if openN == closedN == n:
                result.append("".join(stack))
                return
            
            # Check if we can add more open paranthesis
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            
            # Check if we can add a closing paranthesis
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()
        
        backtrack(0, 0)
        return result
