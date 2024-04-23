class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        
        n = len(profits)

        projects = sorted(zip(capital, profits))

        heap = []
        i = 0

        # We can do at most k projects
        for _ in range(k):

            while i < n and projects[i][0] <= w:
                heapq.heappush(heap, -projects[i][1])
                i += 1
            
            # Not enough money to do any more projects
            if len(heap) == 0:
                return w
            
            # Minus because we added the minus signs to the heap
            w -= heapq.heappop(heap)

        return w