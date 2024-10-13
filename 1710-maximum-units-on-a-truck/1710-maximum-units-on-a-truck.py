import heapq

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:

        minHeap = []

        for i in range(len(boxTypes)):
            boxes, units = boxTypes[i]
            heapq.heappush(minHeap, [-units, boxes])   

        ans = 0

        while minHeap and truckSize > 0:

            units, boxes = heapq.heappop(minHeap)
            units = -units

            while boxes > 0 and truckSize > 0:
                ans += units
                boxes -= 1
                truckSize -= 1
            
        return ans
            

        