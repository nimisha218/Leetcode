from collections import defaultdict
import heapq

class Solution:
    def frequencySort(self, s: str) -> str:
        
        freq = Counter(s)
        
        maxHeap = []
        heapq.heapify(maxHeap)

        for key in freq:
            heapq.heappush(maxHeap, [-freq[key], key])

        result = []

        while maxHeap:

            freq, character = heapq.heappop(maxHeap)
            freq = -freq
            result.append(freq*character)
        
        return "".join(result)
