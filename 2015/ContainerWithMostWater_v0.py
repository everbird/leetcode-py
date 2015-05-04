#!/usr/bin/env python
# encoding: utf-8

class Solution:
    # @param {integer[]} height
    # @return {integer}
    def maxArea(self, height):
        s = sorted([(i, v) for i, v in enumerate(height)], key=lambda x: x[1])
        max_area = 0
        maxa = -1
        maxb = -1
        lenh = len(height)
        for index, v in s:
            n = find_farest(height, index, lenh)
            area = v * abs(n - index)
            if area > max_area:
                max_area = area
                maxa = index
                maxb = n
            height[index] = 0

        return maxa, maxb


def find_farest(a, n, lenh):
    b = 0
    e = lenh - 1
    while a[b] == 0 and b < e:
        b += 1

    while a[e] == 0 and b < e:
        e -= 1

    return b if n - b > (e - n) else e


if __name__ == '__main__':
    #height = [3, 4, 1, 5]
    height = range(1000)
    s = Solution()
    r = s.maxArea(height)
    print r
