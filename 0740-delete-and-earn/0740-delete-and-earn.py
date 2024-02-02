class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:

        nums.sort()

        dp = [0] * len(nums)

        freq = {}

        for el in nums:
            if el in freq:
                freq[el] += 1
            else:
                freq[el] = 1
       
        nums = list(set(nums))

        if len(nums) == 1:
            return nums[0] * freq[nums[0]]
        dp[0] = nums[0] * freq[nums[0]]
        if len(nums) == 2:
            if nums[1] - nums[0] == 1:
                return max(dp[0], (nums[1] * freq[nums[1]]))
            else:
                return dp[0] + nums[1] * freq[nums[1]]
        if nums[1] - nums[0] == 1:
            dp[1] = max(dp[0], (nums[1] * freq[nums[1]]))
        else:
            dp[1] = dp[0] + (nums[1] * freq[nums[1]])
       

        for i in range(2, len(nums)):
            if nums[i] - nums[i-1] == 1:
                dp[i] = max(dp[i-1], ((nums[i] * freq[nums[i]]) + dp[i-2]))
            else:
                dp[i] = dp[i-1] + (nums[i] * freq[nums[i]])
           
        return max(dp)
        
        

        