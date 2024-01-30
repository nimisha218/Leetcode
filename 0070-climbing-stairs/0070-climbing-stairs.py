class Solution:
    def climbStairs(self, n: int) -> int:
        
        dp = [0] * n

        if n == 1:
            return 1

        if n == 2:
            return 2
        
        # Base cases
        dp[0] = 1
        dp[1] = 2

        # Recursive case
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[-1]