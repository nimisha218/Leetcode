class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        result = float('-inf')

        left = 0
        right = 0
        curSum = 0

        for right in range(len(nums)):

            curSum += nums[right]

            result = max(result, curSum)

            if curSum < 0:
                left = right + 1
                curSum = 0
        
        return result

