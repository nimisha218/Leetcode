class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:

        def binary_search(arr, target):

            left = 0
            right = len(arr) - 1

            while left <= right:
                
                mid = (left + right) // 2

                if arr[mid] == target:
                    return mid

                if arr[mid] > target:
                    right = mid - 1
                
                else:
                    left = mid + 1
            
            return right
        
        # Construct a prefix array of nums
        nums.sort()
        prefix_nums = [0] * len(nums)

        
        for i in range(len(nums)):
            prefix_nums[i] = prefix_nums[i-1] + nums[i]

        print("Prefix nums: ", prefix_nums)

        ans = []
        m = len(nums)

        for query in queries:
            right = binary_search(prefix_nums, query)
            ans.append(right + 1)

        return ans