class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            
            if nums[left] < nums[right]:
                if nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            
            else:
                if nums[mid] < nums[right]:
                    if target < nums[mid] or target > nums[right]:
                        right = mid - 1
                    else:
                        left = mid + 1

                else:
                    if target > nums[right]:
                        if target > nums[mid]:
                            left = mid + 1
                        else:
                            right = mid - 1
                    else:
                        left = mid + 1
        
        return -1