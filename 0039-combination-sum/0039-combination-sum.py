class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        def backtrack(curr, total, index):

            if total == target:
                result.append(curr[:])
                return
            
            for i in range(index, len(candidates)):
                if total + candidates[i] <= target:
                    curr.append(candidates[i])
                    backtrack(curr, total + candidates[i], i)
                    curr.pop()
            
        result = []
        backtrack([], 0, 0)
        return result
                