class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # Initialize the dp array
        dp = [amount + 1] * (amount + 1)

        # Base Case
        dp[0] = 0

        # Recurrence Relation
        for a in range(1, amount + 1):
            for c in coins:
                if (a-c) >= 0:
                    dp[a] = min(dp[a], 1 + dp[a-c])
        
        return dp[-1] if dp[-1] != (amount + 1) else -1