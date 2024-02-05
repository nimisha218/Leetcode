class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        rows = m
        cols = n

        dp = [[0] * n for _ in range(m)]
        print("dp: ", dp)

        dp[-1][-1] = 1

        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):

                if dp[i][j] == 1:
                    continue
                
                elif (j+1) >= cols:
                    val = dp[i + 1][j]
                
                elif (i+1) >= rows:
                    val = dp[i][j + 1]
                
                else:
                    val = dp[i+1][j] + dp[i][j+1]

                dp[i][j] = val
        
        return dp[0][0]
                



























        # rows = m
        # cols = n
        
        # # 1
        # dp = [[0] * n for _ in range(m)]

        # # 2
        # dp[-1][-1] = 1
        
        # # 3
        # for row in range(rows - 1, -1, -1):
        #     for col in range(cols - 1, -1, -1):

        #         if dp[row][col] == 1:
        #             continue
        #         if col + 1 >= n:
        #             val = dp[row+1][col]
        #         elif row + 1 >= m:
        #             val = dp[row][col+1]
        #         else:
        #             val = dp[row+1][col] + dp[row][col+1]
        #         dp[row][col] = val
        
        # # 4
        # return dp[0][0]
        