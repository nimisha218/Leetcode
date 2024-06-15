from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        def isValid(row, col):
            return 0 <= row < num_rows and 0 <= col < num_cols
        
        num_rows = len(mat)
        num_cols = len(mat[0])

        queue = deque()
        seen = set()

        for row in range(num_rows):
            for col in range(num_cols):
                if mat[row][col] == 0:
                    queue.append((row, col, 1))
                    seen.add((row, col))
        
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        while queue:

            row, col, steps = queue.popleft()

            for dx, dy in directions:
                new_row = row + dx
                new_col = col + dy
                if isValid(new_row, new_col) and (new_row, new_col) not in seen:
                    queue.append((new_row, new_col, steps + 1))
                    seen.add((new_row, new_col))
                    mat[new_row][new_col] = steps
        
        return mat

    
