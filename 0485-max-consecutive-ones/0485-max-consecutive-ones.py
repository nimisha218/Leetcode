class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        left = 0
        right = 0

        # Find the first one
        for i in range(len(nums)):
            if nums[i] == 1:
                left = i
                break
        
        right = left
        ans = 0
        cur_ans = 0
        
        while right < len(nums):
            if nums[right] == 1:
                cur_ans += 1
                ans = max(ans, cur_ans)
                right += 1
            else:
                left = right + 1
                right = left
                cur_ans = 0

        return ans