class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        # Define a method which checks if the given position is in bounds
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n
        
        # Define a method which checks if we can get from (0,0) to (m-1,n-1) with effort 'effort'
        def check(effort):
            directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
            seen = {(0, 0)}
            stack = [(0, 0)]

            while stack:
                row, col = stack.pop()

                # Check if we are the last square
                if (row, col) == (m - 1, n - 1):
                    return True
                
                for i, j in directions:
                    next_row = i + row
                    next_col = j + col
                    if valid(next_row, next_col) and (next_row, next_col) not in seen:
                        if abs(heights[next_row][next_col] - heights[row][col]) <= effort:
                            seen.add((next_row, next_col))
                            stack.append((next_row, next_col))
                
            return False

        m = len(heights)
        n = len(heights[0])
        
        # Define the search space for our binary search
        left = 0
        right = max([max(row) for row in heights])

        while left <= right:

            mid = (left + right) // 2  

            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
                    
        return left
    