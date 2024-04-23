class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        
        # Sort the input
        nums.sort()

        # Pick the smallest num from the input
        x = nums[0]

        # Set result to 0
        result = 1

        # Iterate over the input
        for i in range(1, len(nums)):

            if nums[i] - x > k:

                x = nums[i]
                result += 1
        
        return result
