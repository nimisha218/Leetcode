from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        d = defaultdict(int)
        d[0] = 1
        curr = 0 
        ans = 0

        for num in nums:
            curr += num
            ans += d[curr - k]
            d[curr] += 1

        return ans

        