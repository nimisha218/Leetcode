class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        # Get the dimensions of the board
        ROWS = len(board)
        COLS = len(board[0])

        # Define an isValid method
        def isValid(row, col):
            return 0 <= row < ROWS and 0 <= col < COLS

        # Define a backtrack method
        def backtrack(row, col, i, seen):
            
            # We found the word
            if i == len(word):
                return True
            
            for r, c in directions:
                next_row = row + r
                next_col = col + c
                if isValid(next_row, next_col) and (next_row, next_col) not in seen:
                    if board[next_row][next_col] == word[i]:
                        seen.add((next_row, next_col))
                        if backtrack(next_row, next_col, i + 1, seen):
                            return True
                        seen.remove((next_row, next_col))
            
            return False

        # Define directions list
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        # Brute force through the entire board as starting positions
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0] and backtrack(r, c, 1, {(r, c)}):
                    return True
        
        return False
            
            
        