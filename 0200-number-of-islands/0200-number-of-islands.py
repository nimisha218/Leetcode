class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])

        result = 0

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    result += 1
                    self.changeToWater(grid, i, j)
                    
        return result
    
    def changeToWater(self, grid, i, j):
  
        if i < 0 or i > len(grid) - 1 or j < 0 or j > len(grid[0]) - 1 or grid[i][j] == "0":
            return 
        
        else:
            grid[i][j] = "0"
            self.changeToWater(grid, i+1, j)
            self.changeToWater(grid, i-1, j)
            self.changeToWater(grid, i, j+1)
            self.changeToWater(grid, i, j-1)

        return
        