class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        # Initialize the sets
        column = set()
        posDiag = set()
        negDiag = set()

        res = []
        board = [["."] * n for i in range(n)]
        
        # Define the backtrack method
        def backtrack(row):

            if row == n:
                temp = ["".join(r) for r in board]
                res.append(temp)
                return
        
            for c in range(n):

                if c in column or (c+row) in posDiag or (c-row) in negDiag:
                    continue
                
                column.add(c)
                posDiag.add(c+row)
                negDiag.add(c-row)
                board[row][c] = "Q"
                backtrack(row + 1)
                board[row][c] = "."
                column.remove(c)
                posDiag.remove(c+row)
                negDiag.remove(c-row)

        backtrack(0)
        return res