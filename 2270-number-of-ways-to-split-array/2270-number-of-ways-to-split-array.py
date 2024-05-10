class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        
        result = 0

        # Compute the prefix sum array
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(prefix[-1] + nums[i])
        
        # Partition the nums array -> O(n)
        for i in range(len(nums) - 1):
            # Compute the left sub-array
            sum_left = prefix[i]
            # Compute the right sub-array
            sum_right = prefix[-1] - prefix[i]
            if sum_left >= sum_right:
                result += 1

        return result
        