from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        def isValid(row, col):
            return 0 <= row < num_rows and 0 <= col < num_cols and maze[row][col] == '.'
        
        num_rows = len(maze)
        num_cols = len(maze[0])

        seen = {(entrance[0], entrance[1])}
        queue = deque([(entrance[0], entrance[1], 1)])

        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        while queue:

            num_nodes = len(queue)

            for _ in range(num_nodes):
                row, col, steps = queue.popleft()
                for dx, dy in directions:
                    new_row, new_col = row + dx, col + dy
                    if isValid(new_row, new_col) and (new_row, new_col) not in seen:
                        if (new_row == num_rows - 1) or (new_col == num_cols - 1) or (new_row == 0) or (new_col == 0):
                            return steps 
                        seen.add((new_row, new_col))
                        queue.append((new_row, new_col, steps + 1))

        return -1

            
