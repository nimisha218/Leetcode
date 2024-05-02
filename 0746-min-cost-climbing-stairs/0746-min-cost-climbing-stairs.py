class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        n = len(cost)

        # Initialize the dp array
        dp = [0] * (n + 1)

        # Base Cases are implicit
        dp[0] = 0
        dp[1] = 0

        # Recurrence relation
        for i in range(2, n + 1):
            dp[i] = min(dp[i-2] + cost[i-2], dp[i-1] + cost[i-1])
        
        return dp[-1]


















        # dp = [0] * (len(cost) + 1)

        # # Recursive Recurrence
        # for i in range(2, len(cost) + 1):
        #     dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        
        # return dp[-1]

