class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(curr, index):
            
            if tuple(sorted(curr)) not in result:
                result.add(tuple(sorted(curr)))
            
            for i in range(index, len(nums)):
                curr.append(nums[i])
                backtrack(curr, i + 1)
                curr.pop()
        
        result = set()
        backtrack([], 0)
        ans = []

        for item in result:
            ans.append(list(item))
        
        return ans
