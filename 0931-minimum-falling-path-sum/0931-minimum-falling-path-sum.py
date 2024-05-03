class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        # Define the recursice dp method - cache it!
        @cache
        def dp(row, col):

            # Base Case -> We are at row == 0
            if row == 0:
                return matrix[row][col]
            
            # Recurrence relation
            ans = float("inf")
            
            if row > 0:
                ans = min(ans, dp(row - 1, col))
                if col > 0:
                    ans = min(ans, dp(row - 1, col - 1))
                if col + 1 < n:
                    ans = min(ans, dp(row - 1, col + 1))
            
            return ans + matrix[row][col]

        m = len(matrix)
        n = len(matrix[0])

        res = float("inf")

        for i in range(n):
            res = min(res, dp(m-1, i))

        return res