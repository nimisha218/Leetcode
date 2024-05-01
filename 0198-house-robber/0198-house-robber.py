class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        
        # Initialize the dp array
        dp = [0] * len(nums)

        # Base cases - we can rob the first two houses independently
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        # Recurrence relation
        for i in range(2, len(nums)):
            # We can rob this house and add the cost of i - 2 th house
            # or, we can choose to skip to rob this house, and just include the i - 1 th house
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        
        return dp[-1]

