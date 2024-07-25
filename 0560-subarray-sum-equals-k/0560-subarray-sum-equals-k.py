from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        d = defaultdict(int)
        total = 0
        d[0] = 1
        result = 0

        for num in nums:

            total += num

            if (total-k) in d:
                result += d[total-k]
            
            d[total] += 1
        
        return result



            


        