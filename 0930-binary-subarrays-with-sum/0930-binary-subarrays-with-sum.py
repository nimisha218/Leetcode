from collections import defaultdict

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        # This is a Prefix Sum problem
        ans = 0
        currentSum = 0

        freq = defaultdict(int)

        for num in nums:

            currentSum += num
            
            if currentSum == goal:
                ans += 1
            
            if currentSum - goal in freq:
                ans += freq[currentSum - goal]
            
            freq[currentSum] += 1
        
        return ans



        
