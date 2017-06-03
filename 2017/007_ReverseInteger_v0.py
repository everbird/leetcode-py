#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        if x < 0:
            min_i = - 1 * 2 ** 31

            r = -1 * self.reverse(-1 * x)
            return r if r > min_i else 0

        max_i = 2 ** 31 - 1

        r = 0
        while x:
            digit = x % 10
            x = x // 10
            r = r * 10 + digit

        return r if r <= max_i else 0


if __name__ == '__main__':
    #a = -123456
    a = 1534236469
    s = Solution()
    print s.reverse(a)
