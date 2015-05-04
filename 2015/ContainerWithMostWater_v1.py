#!/usr/bin/env python
# encoding: utf-8

class Solution:
    # @param {integer[]} height
    # @return {integer}
    def maxArea(self, height):
        lenh = len(height)
        b = 0
        e = lenh - 1
        max_area = 0
        rb = -1
        re = -1
        while b < e:
            t = min(height[b], height[e])
            area = (e - b) * t
            if area > max_area:
                max_area = area
                rb = b
                re = e

            if t == height[e]:
                e -= 1
            else:
                b += 1

        return rb, re


if __name__ == '__main__':
    height = [3, 4, 1, 5]
    #height = range(1000)
    s = Solution()
    r = s.maxArea(height)
    print r
