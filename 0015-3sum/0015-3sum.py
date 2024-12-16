class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        result = []

        nums.sort()

        for i in range(len(nums)):

            if i > 0 and nums[i] == nums[i-1]:
                continue

            first = nums[i]

            left = i + 1
            right = len(nums) - 1

            while left < right:

                total = first + nums[left] + nums[right]

                if total == 0:
                    result.append([first, nums[left], nums[right]])
                    left += 1
                    while left < len(nums) and nums[left] == nums[left - 1]:
                        left += 1
                    right -= 1
                    while right >= 0 and nums[right] == nums[right + 1]:
                        right -= 1
                
                elif total > 0:
                    right -= 1
                
                else:
                    left += 1
        
        return result
                
                


                

            
