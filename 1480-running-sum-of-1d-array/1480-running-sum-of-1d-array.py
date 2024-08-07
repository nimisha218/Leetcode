class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        if not nums:
            return []

        result = [nums[0]]

        for i in range(1, len(nums)):
            result.append(result[-1] + nums[i])
        
        return result