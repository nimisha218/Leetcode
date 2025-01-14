from collections import defaultdict

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        count = defaultdict(int)
        count[0] = 1
        ans = 0
        curr = 0

        for num in nums:
            
            if num % 2:
                curr += 1

            ans += count[curr - k]
            count[curr] += 1
        
        return ans

