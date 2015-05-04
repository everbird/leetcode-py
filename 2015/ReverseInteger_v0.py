#!/usr/bin/env python
# encoding: utf-8


class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        symbol = 1 if x >= 0 else -1
        x = x * symbol

        r = 0
        while x > 0:
            r = r * 10 + (x % 10)
            x = x // 10

        return 0 if r > 2 ** 31 else r * symbol

if __name__ == '__main__':
    a = -123456
    s = Solution()
    print s.reverse(a)
