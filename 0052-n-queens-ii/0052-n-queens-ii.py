class Solution:
    def totalNQueens(self, n: int) -> int:
        
        # Initialize the sets
        column = set()
        positiveDiagonal = set()
        negativeDiagonal = set()

        res = [0]

        board = [["."] * n for i in range(n)]

        # Define the backtrack method
        def backtrack(r):
            
            # We found a solution:
            if r == n:
                res[0] += 1
                return
            
            for c in range(n):

                # Check if invalid position
                if (c in column or
                   (r + c) in positiveDiagonal or
                   (r - c) in negativeDiagonal):

                   continue
                
                # Valid position
                column.add(c)
                positiveDiagonal.add(r + c)
                negativeDiagonal.add(r - c)
                board[r][c] = "Q"

                backtrack(r + 1)

                column.remove(c)
                positiveDiagonal.remove(r + c)
                negativeDiagonal.remove(r - c)
                board[r][c] = "."
        
        backtrack(0)

        return res[0]
