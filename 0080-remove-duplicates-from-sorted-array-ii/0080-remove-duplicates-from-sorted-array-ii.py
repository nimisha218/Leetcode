from collections import defaultdict

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        freq = defaultdict(int)
        count = 0
        found = []

        for i in range(len(nums)):
            freq[nums[i]] += 1
            if freq[nums[i]] > 2:
                count += 1
                found.append(i)
                # This is a problem
                nums[i] = "_"
        
        ans = len(nums) - count

        while count > 0:
            # Find the location of the first "_"
            for i in range(len(nums)):
                if nums[i] == "_":
                    pos = i
                    break
            
            # i -> Current position of "_"
            # Swap i and i + 1
            while i < len(nums) - 1:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                i += 1
            count -= 1
    
        return ans
                