from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        # Base Case
        if grid[0][0] == 1:
            return -1

        # Define an isValid() method
        def isValid(row, col):
            return 0 <= row < num_rows and 0 <= col < num_cols and grid[row][col] == 0
        
        # Compute num_rows and num_cols
        num_rows = len(grid)
        num_cols = len(grid[0])

        # Define the directions list
        directions = [ (1, 0), (0, 1), (-1, 0), (0, -1), (-1, 1), (1, -1), (1, 1), (-1, -1) ]

        # Initialize a seen set with an initial value of (0, 0)
        seen = {(0, 0)}

        # Initialize a queue (row, col, num_steps)
        queue = deque([(0, 0, 1)])
        while queue:
            row, col, steps = queue.popleft()
            if (row, col) == (num_rows - 1, num_cols - 1):
                return steps
            for i, j in directions:
                next_row = i + row
                next_col = j + col
                if (next_row, next_col) not in seen and isValid(next_row, next_col):
                    seen.add((next_row, next_col))
                    queue.append((next_row, next_col, steps + 1))
        
        # Target was never reached successfully
        return -1 

                