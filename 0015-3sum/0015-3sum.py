class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        result = []
        
        for i in range(len(nums)):
            
            if i > 0 and nums[i] == nums[i-1]:
                continue

            currNum = nums[i]

            left = i + 1
            right = len(nums) - 1

            while left < right:

                total = currNum + nums[left] + nums[right]

                if total == 0:
                    result.append([currNum, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                
                elif total < 0:
                    left += 1
                
                else:
                    right -= 1
            
        return result