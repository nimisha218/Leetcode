class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        result = 0

        left = 0

        curr = 1

        if k <= 1:
            return 0

        for right in range(len(nums)):

            curr *= nums[right]

            while curr >= k:
                curr //= nums[left]
                left += 1
            
            result += (right - left + 1)
        
        return result