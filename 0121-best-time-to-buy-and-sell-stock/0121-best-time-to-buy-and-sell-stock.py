class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # Left is buying
        left = 0
        # Right is selling
        right = 1

        maxProfit = 0

        while right < len(prices):
            # If we make profit (buying < selling : left < right)
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxProfit = max(maxProfit, profit)
            else:
                # No profit, so set left to the right pointer
                left = right
            # Increment right at every iteration (increment the selling point)
            right += 1
        
        return maxProfit

            





        
