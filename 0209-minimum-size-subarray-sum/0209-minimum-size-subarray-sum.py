class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        # Build the first valid window
        total = 0
        left = 0
        ans = 0

        for i in range(len(nums)):
            total += nums[i]
            right = i
            if total >= target:
                ans = right - left + 1
                break
        
        # Check if this window is shrinkable
        while total >= target:
            total -= nums[left]
            if total >= target:
                left += 1
                ans = min(ans, right - left + 1)
            else:
                total += nums[left]
                break

        for r in range(right + 1, len(nums)):

            total += nums[r]

            while total >= target and left < len(nums):
                total -= nums[left]
                left += 1
                if total >= target:
                    ans = min(ans, r - left + 1)

        return ans
        