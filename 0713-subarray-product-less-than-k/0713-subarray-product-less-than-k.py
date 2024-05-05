class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        

        if k <= 1:
            return 0
            
        left = 0
        ans = 0

        current = 1

        for right in range(len(nums)):

            current *= nums[right]

            while current >= k:

                # Remove from the left
                current //= nums[left]
                left += 1
            
            ans += right - left + 1
        
        return ans 