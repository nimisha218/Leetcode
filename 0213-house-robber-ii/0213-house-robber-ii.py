class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def rob(nums):

            # Base Cases
            twoBack = nums[0]
            if len(nums) == 1:
                return nums[0]

            oneBack = max(nums[0], nums[1])
            if len(nums) == 2:
                return oneBack

            # Recurrence Relation
            for i in range(2, len(nums)):
                oneBack, twoBack = max(oneBack, nums[i] + twoBack), oneBack
            return oneBack
        
        if len(nums) == 1:
            return nums[0]

        return max(rob(nums[:-1]), rob(nums[1:]))