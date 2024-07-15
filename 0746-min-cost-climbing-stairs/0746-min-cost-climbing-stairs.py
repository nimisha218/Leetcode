from functools import cache

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        @cache
        def dp(i):

            if i == 0 or i == 1:
                return 0
            
            return min(dp(i-1) + cost[i-1], dp(i-2) + cost[i-2])
        
        return dp(len(cost))

















        # dp = [0] * (len(cost) + 1)

        # # Recursive Recurrence
        # for i in range(2, len(cost) + 1):
        #     dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        
        # return dp[-1]

