class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # Define the recursive dp method -> cache it
        @cache
        def dp(i, holding, cooldown):

            # Base case -> We are at the end of the list
            if i == len(prices):
                return 0
            
            # Skip Case -> Do nothing, move to the next day
            if cooldown:
                ans = dp(i+1, holding, False)
            else:
                ans = dp(i+1, holding, cooldown)
            
            # Recurrence Relation
            if holding:
                # We have a stock -> Sell it, trigger cooldown
                ans = max(ans, prices[i] + dp(i+1, False, True))
            else:
                # We don't have a stock -> Buy it
                # BUT -> Check if cooldown period is active first
                if cooldown:
                    # We can't really do anything here -> Wait another day
                    ans = dp(i+1, holding, False)
                else:
                    ans = max(ans, -prices[i] + dp(i+1, True, False))
            
            return ans
        
        return dp(0, False, False)