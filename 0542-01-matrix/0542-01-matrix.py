from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        # Check if the current position is valid or not
        def isValid(row, col):
            return 0 <= row < num_rows and 0 <= col < num_cols and mat[row][col] == 1
        
        # Get the number of rows and columns
        num_rows = len(mat)
        num_cols = len(mat[0])
        
        queue = deque()
        seen = set()
        
        for row in range(num_rows):
            for col in range(num_cols):
                if mat[row][col] == 0:
                    queue.append((row, col, 1))
        
        # Define the directions list
        directions = [ (0, 1), (1, 0), (-1, 0), (0, -1) ]
        
        while queue:
            
            row, col, steps = queue.popleft()
            for i, j in directions:
                next_row = i + row
                next_col = j + col
                if (next_row, next_col) not in seen and isValid(next_row, next_col):
                    if mat[next_row][next_col] == 1:
                        mat[next_row][next_col] = steps
                    seen.add((next_row, next_col))
                    queue.append((next_row, next_col, steps + 1))
        
        return mat