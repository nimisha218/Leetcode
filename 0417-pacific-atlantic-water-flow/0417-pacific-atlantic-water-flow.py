class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        def isValid(row, col):
            return 0 <= row < num_rows and 0 <= col < num_cols

        def dfs(row, col, visit, prevHeight):

            if not isValid(row, col) or (row, col) in visit or heights[row][col] < prevHeight:
                return
            
            visit.add((row, col))

            for dx, dy in directions:
                new_row = row + dx
                new_col = col + dy
                dfs(new_row, new_col, visit, heights[row][col])
            
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        num_rows = len(heights)
        num_cols = len(heights[0])

        pacific = set()
        atlantic = set()
        result = []

        for col in range(num_cols):
            dfs(0, col, pacific, heights[0][col])
            dfs(num_rows - 1, col, atlantic, heights[num_rows - 1][col])
        
        for row in range(num_rows):
            dfs(row, 0, pacific, heights[row][0])
            dfs(row, num_cols - 1, atlantic, heights[row][num_cols - 1])
        
        for pair in pacific:
            if pair in atlantic:
                result.append(list(pair))
        
        return result
        
