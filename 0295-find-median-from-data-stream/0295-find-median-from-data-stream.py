import heapq

class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxHeap, -num)
        num = -heapq.heappop(self.maxHeap)
        heapq.heappush(self.minHeap, num)
        if len(self.minHeap) > len(self.maxHeap):
            num = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -num)

    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            num1 = self.minHeap[0]
            num2 = -self.maxHeap[0]
            return (num1 + num2) / 2
        else:
            return -self.maxHeap[0]
        
        
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()