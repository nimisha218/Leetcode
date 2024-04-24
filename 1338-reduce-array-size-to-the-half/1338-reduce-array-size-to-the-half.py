from collections import Counter
import heapq

class Solution:
    def minSetSize(self, arr: List[int]) -> int:

        heap = []
        
        # Construct a counts hash map
        counts = Counter(arr)

        original_size = len(arr)

        target_size = len(arr) // 2

        for num in counts:
            freq = counts[num]
            heapq.heappush(heap, -freq)
        
        ans = 0

        while original_size > target_size:

            remove = - heapq.heappop(heap)
            original_size -= remove
            ans += 1
        
        return ans
