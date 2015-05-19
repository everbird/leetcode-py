#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[]} height
    # @return {integer}
    def largestRectangleArea(self, height):
        i = 0
        max_a = 0
        s = []
        h = height[:]
        h.append(0)
        while i < len(h):
            if not s or h[i] >= h[s[-1]]:
                s.append(i)
                i += 1
            else:
                t = s.pop()
                v = (i - s[-1] - 1) if s else i # If s is empty, h[t] is the min value, so area is h[t]*i
                max_a = max(max_a, h[t] * v)

        return max_a


if __name__ == '__main__':
    s = Solution()
    print s.largestRectangleArea([2,1,5,6,2,3])
    print s.largestRectangleArea([1,1])
    print s.largestRectangleArea([1,1,1,1,1,1,1,1])
    print s.largestRectangleArea([0,9])
    print s.largestRectangleArea([1,2,2])
