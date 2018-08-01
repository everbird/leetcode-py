import bisect

class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []
        self.cnt = 0


    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        bisect.insort(self.nums, num)
        self.cnt += 1


    def findMedian(self):
        """
        :rtype: float
        """
        if self.cnt % 2 == 1:
            return self.nums[self.cnt // 2]

        a = self.cnt // 2
        b = a - 1
        return (self.nums[a] + self.nums[b]) / 2.0




# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
