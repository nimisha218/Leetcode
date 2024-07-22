class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        total = 0

        # Build the first window
        for i in range(k):
            total += nums[i]

        max_average = total / k

        # Start sliding the window
        left = 0
        right = k

        while right < len(nums):

            total -= nums[left]
            total += nums[right]
            max_average = max(max_average, total / k)
            left += 1
            right += 1
        
        return max_average

