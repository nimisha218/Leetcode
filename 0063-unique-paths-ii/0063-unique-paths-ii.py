class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        # Define the recursive dp method - cache it
        @cache
        def dp(row, col):

            # Base Case -> If we are at (0, 0) -> only 1 way
            if (row, col) == (0, 0):
                return 1
            
            # Recurrence relation
            ways = 0

            if row > 0:
                if obstacleGrid[row-1][col] != 1:
                    ways += dp(row - 1, col)
            if col > 0:
                if obstacleGrid[row][col-1] != 1:
                    ways += dp(row, col - 1)
            return ways

        
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if obstacleGrid[m-1][n-1] == 1:
            return 0
            
        return dp(m-1, n-1)