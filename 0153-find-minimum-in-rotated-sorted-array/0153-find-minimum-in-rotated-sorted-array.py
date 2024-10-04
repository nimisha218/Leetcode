class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left = 0
        right = len(nums) - 1

        result = nums[left]

        while left <= right:

            if nums[left] < nums[right]:
                # We have a sorted section! 
                result = min(result, nums[left])
                break

            mid = (left + right) // 2
            result = min(result, nums[mid])

            if nums[mid] >= nums[left]:
                left = mid + 1
            
            else:
                right = mid - 1
        
        return result