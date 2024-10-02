from collections import defaultdict

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        freq = defaultdict(int)

        for num in nums:
            if freq[num] == 1:
                return True
            freq[num] = 1
        
        return False