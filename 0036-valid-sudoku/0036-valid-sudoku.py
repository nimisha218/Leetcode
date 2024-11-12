from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        n = len(board)

        # Check for cols first
        cols = set()
        for row in range(n):
            cols = set()
            for col in range(n):
                if board[row][col] == ".":
                    continue
                if board[row][col] in cols:
                    return False
                cols.add(board[row][col])
        
        # Check for rows next
        for col in range(n):
            rows = set()
            for row in range(n):
                if board[row][col] == ".":
                    continue
                if board[row][col] in rows:
                    return False
                rows.add(board[row][col])
            
        # Check for sections
        sections = defaultdict(set)
        for row in range(n):
            for col in range(n):
                if board[row][col] == ".":
                    continue
                if board[row][col] in sections[(row // 3, col // 3)]:
                    return False
                sections[(row // 3, col // 3)].add(board[row][col])
            
        return True



        
