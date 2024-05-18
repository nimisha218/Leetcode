from collections import defaultdict

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        
        left = 0
        right = 0

        ans = 0
        curr_ans = 0

        freq = defaultdict(int)

        while right < len(nums):

            num = nums[right]

            freq[num] += 1
            
            # Check if it is an invalid window
            while freq[num] > k:
                # Update HashMap
                freq[nums[left]] -= 1
                left += 1
                curr_ans -= 1
            
            right += 1
            curr_ans += 1
            ans = max(ans, curr_ans)
        
        return ans

