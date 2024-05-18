from collections import defaultdict

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        def fact(n):
            
            if n == 1 or n == 0:
                return 1
            return n * fact(n-1)
        
        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1
        
        count = 0

        for key in freq:
            if freq[key] > 2:
                temp = fact(freq[key]) // (fact(freq[key] - 2) * 2)
                count += temp
            if freq[key] == 2:
                count += 1

        return count