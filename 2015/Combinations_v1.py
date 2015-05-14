#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {integer[][]}
    def combine(self, n, k):
        if k > n:
            return []

        if k == 0:
            return []

        nums = range(1, n+1)
        if k == 1:
            return [[x] for x in nums]

        if k == n:
            return [nums]

        r = []
        for i in range(n - 1, k - 2, -1):
            t = [nums[i]]
            items = self.combine(i, k - 1)
            for item in items:
                r.append(item+t)
        return r


if __name__ == '__main__':
    s = Solution()
    print s.combine(4, 2)
    print s.combine(2, 4)
    print s.combine(2, 2)
    print s.combine(2, 0)
    print s.combine(4, 3)
    print s.combine(2, 1)
    print s.combine(3, 3)
