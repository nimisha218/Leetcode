from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        num_rows = len(board)
        num_cols = len(board[0])

        sections = defaultdict(set)

        # Check for columns
        for row in range(num_rows):
            cols = set()
            for col in range(num_cols):
                if board[row][col] == '.':
                    continue
                if board[row][col] in cols:
                    return False
                cols.add(board[row][col])
        
        # Check for rows
        for col in range(num_cols):
            rows = set()
            for row in range(num_rows):
                if board[row][col] == '.':
                    continue
                if board[row][col] in rows:
                    return False
                rows.add(board[row][col])

        # Check for sections
        for row in range(num_rows):
            for col in range(num_cols):

                if board[row][col] == '.':
                    continue
                
                if board[row][col] in sections[(row // 3, col // 3)]:
                    return False
                
                sections[(row//3, col//3)].add(board[row][col])
        

        return True
