from collections import defaultdict

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        d = defaultdict(int)
        d[0] = 1

        result = 0

        curr = 0

        for num in nums:
            
            if num % 2 == 1:
                curr += 1
            
            result += d[curr - k]

            d[curr] += 1

        return result
        