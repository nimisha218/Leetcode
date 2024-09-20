from functools import cache

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        dp = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):

                if nums[j] > nums[i]:
                    dp[j] = max(dp[j], dp[i] + 1)
        
        return max(dp)








        
        # Top-down approach

        # @cache
        # def dp(i):

        #     ans = 1

        #     for j in range(i):
        #         if nums[i] > nums[j]:
        #             ans = max(ans, dp(j) + 1)
            
        #     return ans
        
        # return max(dp(i) for i in range(len(nums)))

        # Bottom-up implementation
        dp = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
        
        return max(dp)