from collections import defaultdict

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        
        d = defaultdict(int)

        left = 0
        ans = 0

        for right in range(len(nums)):

            if d[nums[right]] >= k: 
                # Shrink the window from the left until we encounter nums[right]
                while nums[left] != nums[right]:
                    d[nums[left]] -= 1
                    left += 1
                d[nums[left]] -= 1
                left += 1
            
            d[nums[right]] += 1
            ans = max(ans, right - left + 1)
        
        return ans


        
