#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[]} height
    # @return {integer}
    def largestRectangleArea(self, height):
        lenh = len(height)
        lefts = [0] * lenh
        rights = [lenh] * lenh
        for i in range(1, lenh):
            p = i - 1
            while 0 <= p < lenh and height[p] >= height[i]:
                p = lefts[p] - 1
            lefts[i] = p + 1

        for i in range(lenh-2, -1, -1):
            p = i + 1
            while 0 <= p < lenh and height[p] >= height[i]:
                p = rights[p]
            rights[i] = p

        max_area = 0
        for i in range(lenh):
            max_area = max(max_area, height[i]*(rights[i] - lefts[i]))

        return max_area


if __name__ == '__main__':
    s = Solution()
    print s.largestRectangleArea([2,1,5,6,2,3])
    print s.largestRectangleArea([1,1])
    print s.largestRectangleArea([1,1,1,1,1,1,1,1])
    print s.largestRectangleArea([0,9])
    print s.largestRectangleArea([1,2,2])
