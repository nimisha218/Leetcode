class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(curr):
            # Base Case
            if len(curr) == len(nums):
                ans.append(curr[:])
                return
            
            # Recursive case
            for num in nums:
                if num not in curr:
                    curr.append(num)
                    backtrack(curr)
                    curr.pop()
            
        ans = []
        backtrack([])
        return ans