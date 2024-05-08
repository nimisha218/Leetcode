class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if len(nums) == 1:
            return nums
        
        i = 0
        j = i + 1

        while j < len(nums) and i < j:

            if nums[i] == 0 and nums[j] == 0:
                j += 1
            
            elif nums[i] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            
            else:
                i += 1
                j += 1
    














        
        # # Make the left pointer point to the first zero
        # for i in range(len(nums)):
        #     left = i
        #     if nums[i] == 0:
        #         break

        # # Make right point to non zero
        # right = left + 1
        # while right < len(nums) and nums[right] == 0:
        #     right += 1

        # while right < len(nums):

        #     # Swap left and right
        #     nums[left], nums[right] = nums[right], nums[left]
        #     left += 1

        #     # Ensure left points at 0
        #     while nums[left] != 0:
        #         left += 1
            
        #     right = left + 1

        #     # Ensure right points at non-zero
        #     while right < len(nums) and nums[right] == 0:
        #         right += 1
        