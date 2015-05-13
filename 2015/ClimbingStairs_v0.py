#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer} n
    # @return {integer}
    def climbStairs(self, n):
        if n == 1:
            return 1

        if n == 2:
            return 2

        c = [0] * n
        c[0] = 1
        c[1] = 2

        for i in range(2, n):
            c[i] = c[i - 1] + c[i - 2]

        return c[n-1]


if __name__ == '__main__':
    s = Solution()
    print s.climbStairs(4)
    print s.climbStairs(1)
