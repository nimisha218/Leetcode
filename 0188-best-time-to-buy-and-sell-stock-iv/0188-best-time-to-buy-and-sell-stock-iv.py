class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        
        # Define the recursive dp method -> cache it!
        @cache
        def dp(i, holding, remain):
            
            # Base Case -> We reached the end of the list OR we are out of transactions
            if i == len(prices) or remain == 0:
                return 0
            
            # Skip Case -> Do nothing, go to next day
            ans = dp(i+1, holding, remain)

            # Recurrence Relation
            if holding:
            # We have a stock -> Sell it
                ans = max(ans, prices[i] + dp(i+1, False, remain - 1))
            else:
            # We don't have a stock -> But it
                ans = max(ans, -prices[i] + dp(i+1, True, remain))
            
            return ans
        
        return dp(0, False, k)
