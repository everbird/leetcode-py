#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {float} x
    # @param {integer} n
    # @return {float}
    def myPow(self, x, n):
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n == 0:
            return 1
        elif n == 1:
            return x

        r = self.myPow(x, n // 2)
        return r*r*x if n % 2 else r*r


if __name__ == '__main__':
    s = Solution()
    print s.myPow(1.2, 2)
    print s.myPow(3.400515, -3)
