#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer[]} height
    # @return {integer}
    def trap(self, height):
        mi, m = max_i(height)
        l = height[:mi + 1]
        r = height[mi:]
        return self._trap(l) + self._trap(r[::-1])


    def _trap(self, height):
        if len(height) < 3:
            return 0

        mi, m = max_i(height[:-1])
        if m == 0:
            return 0

        l = height[:mi + 1]
        r_area = (len(height) - 1 - mi - 1) * min(height[-1], height[mi])
        for n in height[mi + 1:-1]:
            r_area -= n

        return self._trap(l) + r_area


def max_i(nums):
    m = mi = 0
    for i, n in enumerate(nums):
        if m < n:
            m, mi = n, i

    return mi, m


if __name__ == '__main__':
    s = Solution()
    a = [0,1,0,2,1,0,1,3,2,1,2,1]
    print s.trap(a)

    #a = [1,2,1]
    #print s.trap(a)
    #a = [1,2,1,2,3]
    #print s._trap(a)
