from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        queue = deque([])

        result = []

        for i in range(len(nums)):

            if queue and (i - queue[0]) == k:
                queue.popleft()

            while queue and nums[queue[-1]] <= nums[i]:
                queue.pop()
            
            queue.append(i)

            if i + 1 >= k:
                result.append(nums[queue[0]])
            
        return result


            
