import heapq

class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minheap = []
        self.maxheap = []


    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if not self.maxheap or num <= -self.maxheap[0]:
            heapq.heappush(self.maxheap, -num)
        else:
            heapq.heappush(self.minheap, num)

        min_len = len(self.minheap)
        max_len = len(self.maxheap)
        if not (min_len == max_len) and not (max_len - min_len == 1):
            if max_len > min_len:
                val = heapq.heappop(self.maxheap)
                heapq.heappush(self.minheap, -val)
            else:
                val = heapq.heappop(self.minheap)
                heapq.heappush(self.maxheap, -val)


    def findMedian(self):
        """
        :rtype: float
        """
        min_len = len(self.minheap)
        max_len = len(self.maxheap)
        if min_len == max_len:
            return (self.minheap[0] - self.maxheap[0]) / 2.0

        return -self.maxheap[0]




# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
if __name__ == '__main__':
    obj = MedianFinder()
    obj.addNum(1)
    obj.addNum(2)
    print obj.findMedian()
    obj.addNum(3)
    print obj.findMedian()
