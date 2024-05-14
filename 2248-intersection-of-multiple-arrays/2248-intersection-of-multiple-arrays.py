from collections import defaultdict

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        
        d = defaultdict(int)
        result = []
        
        for arr in nums:
            for num in arr:
                d[num] += 1
        
        for key in d:
            if d[key] == len(nums):
                result.append(key)
        
        result.sort()
        
        return result
                
            
        