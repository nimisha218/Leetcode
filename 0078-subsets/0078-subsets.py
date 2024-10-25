class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(curr, index):

            result.append(curr[:])

            for i in range(index, len(nums)):
                curr.append(nums[i])
                backtrack(curr, i + 1)
                curr.pop()
        
        result = []
        backtrack([], 0)
        return result

