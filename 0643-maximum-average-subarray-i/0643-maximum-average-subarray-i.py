class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        total = 0
        # Build the first valid window
        for i in range(k):
            total += nums[i]
        
        # Compute the average of the first valid window
        avg = 0
        avg = total / k

        left = 0
        # Start iterating over the next windows
        for i in range(k, len(nums)):

            total += nums[i]
            total -= nums[left]
            left += 1
            avg = max(avg, total / k)
        
        return avg