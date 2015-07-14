#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {integer[][]}
    def combine(self, n, k):
        if k == 0 or k > n:
            return []

        nums = range(1, n+1)
        if k == 1:
            return [[x] for x in nums]

        if k == n:
            return [nums]

        r = []
        for i in range(n):
            num = nums[i]
            for item in self.combine(i, k-1):
                r.append(item+[num])

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
