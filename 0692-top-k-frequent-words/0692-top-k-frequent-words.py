import heapq
from collections import defaultdict

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        heap = []
        heapq.heapify(heap)

        d = defaultdict(int)

        for word in words:
            d[word] += 1
        
        for key in d:
            item = [-d[key], key]
            heapq.heappush(heap, item)

        result = []
        
        while heap and k > 0:
            item = heapq.heappop(heap)
            result.append(item[1])
            k -= 1

        return result