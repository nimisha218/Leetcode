from collections import defaultdict

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        
        d = defaultdict(int)

        for num in nums:
            d[num] += 1
        
        ans = 0
        
        for key in d:
            if d[key] == 1:
                ans += key

        return ans
       


