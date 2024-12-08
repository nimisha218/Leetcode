class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        n = len(nums)

        currSum = sum(nums)

        expSum = sum([num for num in range(n+1)])

        return expSum - currSum

        # res = 0

        # for i in range(len(nums) + 1):
        #     res = res ^ i
        
        # for num in nums:
        #     res = res ^ num
        
        # return res