#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[]} height
    # @return {integer}
    def largestRectangleArea(self, height):
        lenh = len(height)
        if not lenh:
            return 0

        if lenh == 1:
            return height[0]

        b = 0
        e = lenh - 1
        max_a = max(height)
        while b <= e:
            v = min(height[b:e+1])
            area = v * (e - b + 1)
            if max_a < area:
                max_a = area

            if height[e] > height[b]:
                while (b+1) <= e and height[b] >= height[b+1]:
                    b += 1

                b += 1
            else:
                while (e-1) >= b and height[e] > height[e-1]:
                    e -= 1

                e -= 1

        return max_a


if __name__ == '__main__':
    s = Solution()
    print s.largestRectangleArea([2,1,5,6,2,3])
    print s.largestRectangleArea([1,1])
    print s.largestRectangleArea([1,1,1,1,1,1,1,1])
    print s.largestRectangleArea([0,9])
    print s.largestRectangleArea([1,2,2])
