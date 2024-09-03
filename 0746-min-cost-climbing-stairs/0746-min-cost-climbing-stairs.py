from functools import cache

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        # Top-Down Approach
        @cache
        def dp(i):

            if i <= 1:
                return 0
            
            return min(dp(i-1) + cost[i-1], dp(i-2) + cost[i-2])   
                 
        return dp(len(cost))
            

