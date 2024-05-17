from collections import defaultdict

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        
        d = defaultdict(int)

        max_freq = 0
        for num in nums:
            d[num] += 1
            if d[num] >= max_freq:
                max_freq = d[num]
        
        ans = 0
        for num in nums:
            if d[num] == max_freq:
                ans += 1
                
        return ans