from collections import defaultdict

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(prefix[-1] + nums[i])

        d = defaultdict(int)
        d[0] = 1
        ans = 0

        for total in prefix:

            if (total - goal) in d:
                ans += d[total-goal]
                d[total] += 1

            else:
                d[total] += 1

        return ans
            


            
       

        
