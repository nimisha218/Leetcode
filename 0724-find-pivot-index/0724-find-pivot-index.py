class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        # Compute the prefix array
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(prefix[-1] + nums[i])
        
        # Partition the array
        for i in range(len(nums)):

            # Edge Case
            if i == 0:
                sum_left = 0
            else:
                sum_left = prefix[i-1]
                
            # Edge Case 2
            if i == len(nums) - 1:
                sum_right = 0
            else:
                sum_right = prefix[-1] - prefix[i]

            if sum_left == sum_right:
                return i

        return -1
