from functools import cache

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        # Top-down approach (Start from the result case and work your way DOWN to the base case)

        def dp(i):
            
            # Base Case -> Can start from index 0 or 1
            if i <= 1:
                return 0
            
            # Check if the state was already computed
            if i in memo:
                return memo[i]
            
            # Define the recurrence relation
            memo[i] = min(dp(i-1) + cost[i-1], dp(i-2) + cost[i-2])
            return memo[i]
        
        memo = {}
        return dp(len(cost))

